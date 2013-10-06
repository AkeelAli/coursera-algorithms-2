
f = open('g3.txt', 'r')

lines = f.readlines()

f.close()

n, m = lines[0].split(' ')
n, m = int(n), int(m)

edges_h = {}
vertices = []
for line in lines[1:]:
	u, v, c = line.split(' ')
	u, v, c = int(u), int(v), int(c)

	edges_h[(u, v)] = c
	if u not in vertices:
		vertices.append(u)
	if v not in vertices:
		vertices.append(v)

vertices = sorted(vertices)
print "We have %d vertices and %d edges" % (n, m)

INF = 999999

fw = {}
for i in vertices:
	fw[i] = {}
	for j in vertices:
		if (i,j) in edges_h:
			fw[i][j] = edges_h[(i,j)]
		elif i == j:
			fw[i][j] = 0
		else:
			fw[i][j] = INF

min_path = INF
for k in vertices:
	print "Processing k=%d of %d vertices" %(k, len(vertices))
	for i in vertices:
		for j in vertices:
			fw[i][j] = min(fw[i][j],fw[i][k] + fw[k][j])
		
			if fw[i][j] < min_path:
				min_path = fw[i][j]

print "Min path = %d" % min_path

#detect negative cycle
for i in vertices:
	if fw[i][i] < 0:
		print "Detected negative cycle"
		exit()

print "No negative cycle"

