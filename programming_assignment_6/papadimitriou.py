f = open('2sat1.txt', 'r')
lines = f.readlines()
f.close()

num_vars = int(lines[0])

clauses = []
processed_clauses = []
var_sign = {}

for line in lines[1:]:
	vars = line.split(' ')
	var1, var2 = int(vars[0]), int(vars[1])

	clauses.append((var1, var2))

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
	

print len(clauses)

		
for clause in clauses:
	if ( (clause[0] not in var_sign) or (clause[0] in var_sign and var_sign[clause[0]] == -2) ) and \
	   ( (clause[1] not in var_sign) or (clause[1] in var_sign and var_sign[clause[1]] == -2) ):
		processed_clauses.append(clause)	
	#add elifs to set the values of clause[0] or clause[1]


#to_eliminate_global = []
#for var in range(1, num_vars + 1):
#	print "Processing %d from %d" % (var, num_vars)
#	is_positive = 0
#	to_eliminate_local = []
#	to_be_eliminated = True
#	for clause in clauses:
#		if var == abs(clause[0]):
#			if (clause[0] < 0 and is_positive == 1) or (clause[0] > 0 and is_positive == -1):
#				to_be_eliminated = False
#				break
#			else:
#				if (clause[0] < 0):
#					is_positive = -1
#				else:
#					is_positive = 1
#
#				to_eliminate_local.append(clause)
#
#		elif var == abs(clause[1]):
#			if (clause[1] < 0 and is_positive == 1) or (clause[1] > 0 and is_positive == -1):
#				to_be_eliminated = False
#				break
#			else:
#				if (clause[1] < 0):
#					is_positive = -1
#				else:
#					is_positive = 1
#
#				to_eliminate_local.append(clause)
#
#	if to_be_eliminated:
#		#SET value of variable forever (based on is_positive) or simply discard that variable
#		to_eliminate_global += to_eliminate_local
#
#for clause in to_eliminate_global:
#	clauses.remove(clause)

print len(processed_clauses)
