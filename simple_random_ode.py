from pde import *
import math
import numpy as np
import pylab as plt
a=0
b=1

n=2000

spatial_step_x=(b-a)/float(n)
t_list=onedinterval(a,b,spatial_step_x,n)
#print t_list

trials=1000

solutionList=[]

for i in range(0,trials):
	solution_this_trial=[]
	intital_condition = np.random.uniform(0,2)
	print intital_condition
	#intital_condition = np.random.exponential(5.0)
	solution_this_trial.append(intital_condition)
	for i in range(0,len(t_list)):
		solution_this_trial.append( solution_this_trial[i]*(1.0+spatial_step_x))
	solutionList.append(solution_this_trial)

average_sol=[]
for j in range(0,len(t_list)):
	average=0
	for i in range(0,len(solutionList)):
	
		average=average+solutionList[i][j]
	average_sol.append( average/float(len(solutionList) +1))
variance_sol=[]
for j in range(0,len(t_list)):
	var_list=[]
	for i in range(0,len(solutionList)):
		var_list.append(solutionList[i][j])
	variance_sol.append(np.var(var_list))


print variance_sol[0]
print average_sol[0]
plt.plot(t_list,average_sol)
plt.plot(t_list,variance_sol)
plt.show()




