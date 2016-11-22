# We need networkx installed and PyGMO compiled with the keplerian_toolbox option activated
# Also start this in ipython with the --pylab option
from PyGMO import *
from matplotlib.pyplot import savefig, close

#We instantiate the GTOP problem called cassini_1
prob = problem.cassini_1()

#We instantiate the algorithm Differential Evolution fixing 10 generations for each call
algo = algorithm.de(gen=10)

#Here we instantiate the archipelago with 490 islands an 20 individuals per island .....
archi = archipelago(algo,prob,490,20,topology = topology.ageing_clustered_ba(a=25))

#We can draw an archipelago like this
pos  = archi.draw(n_size=10, scale_by_degree=True, e_alpha=0.03)
savefig('archi000')
close()

#And we start the evolution loops (each evolve will advance each island 10 generation)
for i in range(200):
        #this opens 490 threads ..... each one evolving its population using algo!!!
        archi.evolve(1)
        archi.join()
        print "Drawing " + str(i) + "-th evolution .."
        pos = archi.draw(layout = pos, scale_by_degree=True, n_size=10, e_alpha=0.03)
        savefig('archi%03d' % i, dpi = 72);
        close()