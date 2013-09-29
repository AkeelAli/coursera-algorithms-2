#finds the minimum average search time
def find_min(i, j, s, l):
	if ( i == j ):
		print "%sLeaf %d returning %d" % (s, i, l* p[i])
		return l * p[i]
	else:
		# let each node be root
		minimum = -1
		min = {}
		for r in range(i , j + 1):
			print "%sLetting %d be root" % (s, r)
			min_left = 0
			min_right = 0
			
			if ( r > i):
				min_left =  find_min(i, r - 1, s + " ", l + 1)
			if ( r < j):
				min_right =  find_min(r + 1, j, s + " ", l + 1)
			
			min[r] = l * p[r] + min_left + min_right

			print "%ssumming %d and %d and %d" % (s, l*p[r], min_left, min_right)
			print "%smin[%d] = %d" % (s, r, min[r])


			if minimum == -1:
				minimum = min[r]
			else:
				if min[r] < minimum:
					minimum = min[r]

		print "returning %d" % minimum
		print "\n"

		return minimum


p = [0.05, 0.4, 0.08, 0.04, 0.1, 0.1, 0.23]

#p = [1, 2, 3] 

print find_min(0,6, "", 1)
