class UnionFind():
	
	def __init__(self, edges):
		self.node_to_leader = {}
		self.leader_to_size = {}
		self.num_leaders = 0
	
		for edge in edges:
			if edge[0] not in self.node_to_leader:
				self.node_to_leader[edge[0]] = edge[0]
				self.leader_to_size[edge[0]] = 1
				self.num_leaders += 1
			if edge[1] not in self.node_to_leader:
				self.node_to_leader[edge[1]] = edge[1]
				self.leader_to_size[edge[1]] = 1
				self.num_leaders += 1

	def get_leader(self, node):
		return self.node_to_leader[node]

	def have_same_leader(self, node1, node2):
		if self.get_leader(node1) == self.get_leader(node2):
			return True
		else:
			return False
	
	# merges groups that those two nodes belong to
	def merge(self, node1, node2):
		if self.leader_to_size[node1] > self.leader_to_size[node2]:
			old_leader = self.get_leader(node2)
			new_leader = self.get_leader(node1)

		else:
			old_leader = self.get_leader(node1)
			new_leader = self.get_leader(node2)

		for key in self.node_to_leader:
			if self.node_to_leader[key] == old_leader:
				self.node_to_leader[key] = new_leader
				self.leader_to_size[old_leader] -= 1
				self.leader_to_size[new_leader] += 1

		self.num_leaders -= 1


from time import localtime

def uint_from_bits(bits, bits_per_node):
	num = 0
	for i in range(0, bits_per_node):
		exponent = bits_per_node - i - 1
		num += int(bits[i]) * 2**exponent
	
	return num

def flip_bit(bits, i):
	if bits[i] == '1':
		bits[i] = '0'
	else:
		bits[i] = '1'

def print_progress(node_id):
	if node_id % 1000 == 0:
		time = localtime()
		print "Processing %d at %d:%d:%d" % (node_id, time[3], time[4], time[5])


#(1) Read file
f = open('clustering_big.txt', 'r')
#f = open('clustering_big_T1.txt', 'r') #ANS 45
#f = open('clustering_big_T2.txt', 'r') #ANS 4
lines = f.readlines()
f.close()

num_nodes, bits_per_node = lines[0].split(' ')
num_nodes, bits_per_node = int(num_nodes), int(bits_per_node)


uint_2_nodeids = {}
nodeid_2_uint = {}
uint_2_bits = {}

node_id = 1
for line in lines[1:]:
	bits = line.split(' ')
	if bits[-1] == "\n":
		bits.pop(-1)
	elif '\n' in bits[-1]:
		bits[-1] = bits[-1].split('\n')[0]

	#sanity
	#assert len(bits) == bits_per_node, "The given bits per node at the beginning of the file %d doesn't match the actual %d bits per node" % (bits_per_node, len(bits))

	#construct an unsigned integer out of the bits
	uint = uint_from_bits(bits, bits_per_node)

	if uint in uint_2_nodeids:
		uint_2_nodeids[uint].append(node_id)
	else:
		uint_2_nodeids[uint] = [node_id]

	nodeid_2_uint[node_id] = uint
	uint_2_bits[uint] = bits

	node_id += 1
	


edges = []
for node_id in range(1, num_nodes + 1):
	# 0 bit hamming difference 
	cost = 0
	uint = nodeid_2_uint[node_id]
	nodes_with_same_uint = uint_2_nodeids[uint]
	
	for node_id_2 in nodes_with_same_uint:
		if node_id_2 != node_id:
			if [node_id_2, node_id, cost] not in edges:
				edges.append([node_id, node_id_2, cost])



for node_id in range(1, num_nodes + 1):
	print_progress(node_id)
	# 1 bit hamming difference
	cost = 1

	#get bit pattern for this node_id
	uint = nodeid_2_uint[node_id]
	bits = uint_2_bits[uint]

	#generate all possible bit pattern differences
	#and check uint_2_nodeids to see if we have matches
	#then add all of these matches
	new_bits = bits[:]
	for i in range(0, bits_per_node):
		flip_bit(new_bits, i)
	
		uint_2 = uint_from_bits(new_bits, bits_per_node)

		if uint_2 in uint_2_nodeids:
			for node_id_2 in uint_2_nodeids[uint_2]:
				if node_id_2 != node_id:
					if [node_id_2, node_id, cost] not in edges:
						edges.append([node_id, node_id_2, cost])
		
		flip_bit(new_bits, i)


for node_id in range(1, num_nodes + 1):
	print_progress(node_id)
	# 2 bits hamming difference
	cost = 2

	#get bit pattern for this node_id
	uint = nodeid_2_uint[node_id]
	bits = uint_2_bits[uint]

	#generate all possible bit pattern differences
	#and check uint_2_nodeids to see if we have matches
	#then add all of these matches
	new_bits = bits[:]
	for i in range(0, bits_per_node):
		flip_bit(new_bits, i)

		for j in range(i + 1, bits_per_node):
			flip_bit(new_bits, j)
	
			uint_2 = uint_from_bits(new_bits, bits_per_node)

			if uint_2 in uint_2_nodeids:
				for node_id_2 in uint_2_nodeids[uint_2]:
					if node_id_2 != node_id:
						if [node_id_2, node_id, cost] not in edges:
							edges.append([node_id, node_id_2, cost])

			# Must reflip the bits before next iteration!
			flip_bit(new_bits, j)
		
		flip_bit(new_bits, i)

				
		

# build union find
union = UnionFind(edges)

# run the algorithm
clusters = num_nodes
for edge in edges:
	if not union.have_same_leader(edge[0], edge[1]):
		union.merge(edge[0], edge[1])
		clusters -= 1

print clusters	
