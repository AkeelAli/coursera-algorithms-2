#Travelling salesman using randomization + greedy algorithm

import random
import math
import sys

def city_dist(u, v):
	return math.sqrt((u.x - v.x)**2 + (u.y - v.y)**2)

class City:
	
	def __init__(self, id, x, y):
		self.id = id
		self.x = x
		self.y = y
		self.next = None

	def __str__(self):
		return "%d: (%f, %f)" % (self.id, self.x, self.y)
	
class Tour:
	
	def __init__(self, first_city, second_city):
		first_city.next = second_city
		second_city.next = first_city
		self.tour_cities = [first_city, second_city]
		self.length = 2 * city_dist(first_city, second_city)

	def add_to_tour(self, from_city, added_city, increment):
		added_city.next = from_city.next
		from_city.next = added_city
		self.tour_cities.append(added_city)
		self.length += increment

#f = open('tc1_4.txt', 'r')
#f = open('tc2_37.txt', 'r')
f = open('tsp.txt', 'r')

lines = f.readlines()

f.close()

num_nodes = int(lines[0])
nodes = []
for line in lines[1:]:
	x, y = line.split(' ')
	x, y = float(x), float(y)
	
	nodes.append((x,y))


cities = {}
#Randomize ids
for id in range(1, num_nodes + 1):
	idx = random.randint(0,len(nodes) - 1)
	node = nodes.pop(idx)	
	
	cities[id] = (City(id, node[0], node[1]))

tour = Tour(cities[1], cities[2])

INF = 999999999
#Probe and Insert by Smallest Increment
def probe_and_insert(id):
	minIncrement = INF 
	insert_after = None

	for u in tour.tour_cities:
		v = u.next

		increment = city_dist(u, cities[id]) + city_dist(cities[id], v) - city_dist(u, v)

		if (increment < minIncrement):
			minIncrement = increment
			insert_after = u
	
	tour.add_to_tour(insert_after, cities[id], minIncrement)
		

for id in range(2, num_nodes + 1):
	probe_and_insert(id)

print tour.length
