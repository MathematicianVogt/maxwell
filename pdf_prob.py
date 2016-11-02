#!/usr/bin/env python
# encoding: utf-8
#Team Ryan and Tyler
import numpy as np
from clawpack import riemann
import math

mx = 200; my = 200
a=-20.0
b=20.0
c=-20.0
d=20.0
k=40.0

deltax=(b-a)/float(mx)
deltay=(d-c)/float(my)


def qinit(state):
    
    X, Y = state.grid.p_centers
    state.q[0,:,:] = (4.0/(3.0*math.pi))*np.exp((-8.0/9.0)*(X-(4.0*math.pi)/(5.0))**2 - 2.0*Y**2)
                


def custom_bc(state, dim, t, qbc, auxbc, num_ghost):
    #print dim 
    qbc[0,:,:] = 0.0



def set_aux(state):
    X,Y = state.grid.p_centers
    aux = np.empty((2,mx,my),order='F')
    aux[0,:,:] = Y
    aux[1,:,:] = -Y - k*np.sin(X)
    
    return aux

def source(solver,state,dt):
# Source: D(t)q_yy, where D(t) = (1/101)*np.sin(10*t)(10*np.exp(-t)+np.sin(10*t)-10*np.cos(10*t))
#Long term question - have the source correct in the interior of the domain. Solution doesn't reach boundaies -Ryan.
    q   = state.q
    dq = np.empty(q.shape)
    current_t=state.t
    D = (1.0/101.0)*math.sin(10.0*current_t)*(10.0*math.exp(-current_t) + math.sin(10.0*current_t) -10*math.cos(10.0*current_t))
    dq[0,:,:]=q[0,:,:]
    for i in range(1,mx-1):
        for j in range(1,my-1):
            dq[0,:,:] = D*((q[0,i,j-1]  -2.0*q[0,i,j] +q[0,i,j+1])/deltay**2)

    return dq

def setup(use_petsc=False,outdir='./_output',solver_type='classic'):

    if use_petsc:
        import clawpack.petclaw as pyclaw
    else:
        from clawpack import pyclaw
    solver = pyclaw.ClawSolver2D(riemann.vc_advection_2D)

    solver.bc_lower[0] = pyclaw.BC.periodic 
   # solver.user_bc_lower = custom_bc
    solver.bc_upper[0] = pyclaw.BC.periodic 
   # solver.user_bc_upper = custom_bc
    
    
    

   #Long term question - waves do not reach boundaries, so BC are not important -Ryan.
    solver.bc_lower[1] = pyclaw.BC.periodic 
    #solver.user_bc_lower = custom_bc
    solver.bc_upper[1] = pyclaw.BC.periodic 
    #solver.user_bc_upper = custom_bc
    
   
    solver.aux_bc_lower[0]=pyclaw.BC.periodic 
    solver.aux_bc_upper[0]=pyclaw.BC.periodic
    solver.aux_bc_lower[1]=pyclaw.BC.periodic
    solver.aux_bc_upper[1]=pyclaw.BC.periodic


    
    solver.dt_initial = 0.1
    solver.cfl_max = .5
    solver.cfl_desired = .5
    solver.step_source = source

    # Domain:


    x = pyclaw.Dimension(a,b,mx,name='x')
    y = pyclaw.Dimension(c,d,my,name='y')
    domain = pyclaw.Domain([x,y])

    

    num_eqn = 1
    num_aux=2
    state = pyclaw.State(domain,num_eqn,num_aux)
    state.aux= set_aux(state)
    qinit(state)

    claw = pyclaw.Controller()
    claw.tfinal = 2.0
    claw.solution = pyclaw.Solution(state,domain)
    claw.solver = solver
    claw.outdir = outdir
    claw.setplot = setplot
    claw.keep_copy = True
    claw.num_output_times=50

    return claw


def setplot(plotdata):
    """ 
    Plot solution using VisClaw.
    """ 
    from clawpack.visclaw import colormaps

    plotdata.clearfigures()  # clear any old figures,axes,items data

    # Figure for pcolor plot
    plotfigure = plotdata.new_plotfigure(name='q[0]', figno=0)

    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes()
    plotaxes.title = 'q[0]'
    plotaxes.scaled = True

    # Set up for item on these axes:
    plotitem = plotaxes.new_plotitem(plot_type='2d_pcolor')
    plotitem.plot_var = 0
    plotitem.pcolor_cmap = colormaps.yellow_red_blue
    plotitem.pcolor_cmin = 0.0
    plotitem.pcolor_cmax = 1.0
    plotitem.add_colorbar = True
    
    # Figure for contour plot
    plotfigure = plotdata.new_plotfigure(name='contour', figno=1)

    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes()
    plotaxes.title = 'q[0]'
    plotaxes.scaled = True

    # Set up for item on these axes:
    plotitem = plotaxes.new_plotitem(plot_type='2d_contour')
    plotitem.plot_var = 0
    plotitem.contour_nlevels = 20
    plotitem.contour_min = 0.01
    plotitem.contour_max = 0.99
    plotitem.amr_contour_colors = ['b','k','r']
    
    return plotdata

    
if __name__=="__main__":
    from clawpack.pyclaw.util import run_app_from_main
    output = run_app_from_main(setup,setplot)