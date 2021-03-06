import random
import math

f = open('2sat6.txt', 'r')
lines = f.readlines()
f.close()

num_vars = int(lines[0])
	
clauses = []
for line in lines[1:]:
	vars = line.split(' ')
	var1, var2 = int(vars[0]), int(vars[1])

	clauses.append((var1, var2))

print "Number of clauses at start %d" % len(clauses)
#Pre-processing Step to Reduce Clauses
while True:
	did_filter = False
	var_sign = {}
	processed_clauses = []

	for clause in clauses:
		var1, var2 = clause[0], clause[1]

		if abs(var1) not in var_sign:
			if var1 < 0:
				var_sign[abs(var1)] = -1
			else:
				var_sign[abs(var1)] = 1
		elif var_sign[abs(var1)] != -2:
			if var1 < 0 and var_sign[abs(var1)] == 1:
				var_sign[abs(var1)] = -2
			elif var1 > 0 and var_sign[abs(var1)] == -1:
				var_sign[abs(var1)] = -2
		
		if abs(var2) not in var_sign:
			if var2 < 0:
				var_sign[abs(var2)] = -1
			else:
				var_sign[abs(var2)] = 1
		elif var_sign[abs(var2)] != -2:
			if var2 < 0 and var_sign[abs(var2)] == 1:
				var_sign[abs(var2)] = -2
			elif var2 > 0 and var_sign[abs(var2)] == -1:
				var_sign[abs(var2)] = -2
		
	
	for clause in clauses:
		if ( (abs(clause[0]) not in var_sign) or (abs(clause[0]) in var_sign and var_sign[abs(clause[0])] == -2) ) and \
		   ( (abs(clause[1]) not in var_sign) or (abs(clause[1]) in var_sign and var_sign[abs(clause[1])] == -2) ): 
			processed_clauses.append(clause)	
		else:
			did_filter = True
			#add elifs to set the values of clause[0] or clause[1]
		
	clauses = processed_clauses

	if not did_filter:
		break
	

print "Number of clauses after pre-processing %d" % len(clauses)


if len(clauses) == 0:
	print "Satisfiable (simply thru preprocessing!)"
	exit(0)


# Run Papadimitriou

variables = {}
for clause in clauses:
	var1, var2 = abs(clause[0]), abs(clause[1])
	
	if var1 not in variables:
		variables[var1] = 0 #random.randint(0,1)
	if var2 not in variables:
		variables[var2] = 0 #random.randint(0,1)

n = len(variables)
num_tries = int(math.log(n,2)) + 1
for i in range(num_tries):
	print "Try %d of %d" % (i + 1,num_tries)
	#INIT
	for var in variables:
		variables[var] = random.choice([-1,1])

	for j in range(2*n**2):
		clauses_met = True
		for clause in clauses:
			var1, var2 = abs(clause[0]), abs(clause[1])

			if ( variables[var1] != clause[0]/abs(clause[0]) ) and ( variables[var2] != clause[1]/abs(clause[1]) ):
				random_pick = random.choice([var1, var2])
				variables[random_pick] = -1 * variables[random_pick]
				clauses_met = False
				break

		if clauses_met:
			print "Satisfiable!"
			print clauses
			print variables
			exit(0)

print "Unsatisfiable"
