# For problems 3 & 4, run this multiple times (adjusting the knobs if necessary)
# to find the highest c ratio you can get thru random experimentation. The actual
# c value can be higher, but not lower (so answer accordingly)

import random

#CONSTANTS
TRIES = 10
MIN_JOBS = 3
MIN_MACHINES = 2
MIN_JOB_SIZE = 1



#KNOBS
MAX_JOBS = 30
MAX_MACHINES = 10
MAX_JOB_SIZE = 20


jobs = []
num_jobs = random.randint(MIN_JOBS,MAX_JOBS)
num_machines = random.randint(MIN_MACHINES,MAX_MACHINES)

for i in range(0,num_jobs):
	jobs.append(random.randint(MIN_JOB_SIZE,MAX_JOB_SIZE))


print jobs
print "Num machines = %d" % num_machines

def find_min_load_machine():
	min_load = machines[0]
	min_machine = 0

	for i in range(1, len(machines)):
		if machines[i] < min_load:
			min_machine = i
			min_load = machines[i]
	
	return min_machine
		

#max_makespan over all tries
max_makespan = 0
max_makespan_question4 = 0
min_makespan = 999999 

for tries in range(TRIES):
	#INIT
	machines = []
	for i in range(0, num_machines):
		machines.append(0)

	# Shuffle jobs to get different results (hopefully hitting max and min makespan)
	random.shuffle(jobs)
    
	# maximum load of a machine
	makespan = 0
    
	for job in jobs:
		min_machine = find_min_load_machine()
    	
		machines[min_machine] += job
    
		if machines[min_machine] > makespan:
			makespan = machines[min_machine]
	
	if makespan > max_makespan:
		max_makespan = makespan
	
	if makespan < min_makespan:
		min_makespan = makespan

#Run it once for problem 4 (i.e with jobs sorted)
#INIT
machines = []
for i in range(0, num_machines):
	machines.append(0)

#Sort jobs for problem 4
jobs.sort(reverse = True)
    
# maximum load of a machine
makespan = 0
    
for job in jobs:
	min_machine = find_min_load_machine()
    	
	machines[min_machine] += job

	if machines[min_machine] > makespan:
		makespan = machines[min_machine]

max_makespan_question4 = makespan

if makespan < min_makespan:
	min_makespan = makespan


question3_ratio = max_makespan * 1.0 / min_makespan
question4_ratio = max_makespan_question4 * 1.0 / min_makespan

print "Question 3 c >= " + str(question3_ratio)
print "Question 4 c >= " + str(question4_ratio)
