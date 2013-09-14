# PRIM's Minimum Spanning Tree Algorithm

#Algorithm description (Slow O(mn) implementation)
#Initialize X = {s}
#T = []
#While X != V:
#	Let e = (u, v) be the cheapest edge of G with u in X and v not in X
#	Add edge e to T
#	Add node v to X

# This code doesn't keep track of T, it simply computes the total min cost

# (1) Parse file and build X and list of edges (assumes each edge is unique and isn't repeated)
X = []
edges = []
f = open('edges.txt', 'r')

lines = f.readlines()

num_nodes, num_edges = lines[0].split(' ')
num_nodes = int(num_nodes)
num_edges = int(num_edges)

for line in lines[1:]:
	u,v,cost = line.split(' ')
	u, v, cost = int(u), int(v), int(cost)

	edge = [u, v, cost]

	edges.append(edge)

f.close()


# (2) While loop to reach all nodes via chepest edges
total_cost = 0
X.append(1)
while len(X) < num_nodes:
	# find cheapest edge with u in x and v not in X
	min_edge_cost = 999999999
	for edge in edges:
		u, v, cost = edge[0], edge[1], edge[2]
		if (u in X) and (v not in X) and (cost < min_edge_cost):
			min_edge_cost = cost
			min_edge = edge
			node_reached = v
		elif (u not in X) and (v in X) and (cost < min_edge_cost):
			min_edge_cost = cost
			min_edge = edge
			node_reached = u

	total_cost += min_edge_cost
	edges.remove(min_edge)
	X.append(node_reached)

	print "Processed %d nodes" % len(X)

print "Cost of minimum spanning tree = " + str(total_cost)


		


