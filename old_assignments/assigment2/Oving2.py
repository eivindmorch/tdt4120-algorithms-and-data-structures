from sys import stdin
from random import randint
# import time

# start_time = time.clock()
True = 1
False = 0

class Node:
	barn = None 
	ratatosk = None
	depth = None
	def __init__(self):
		self.barn = []
		self.ratatosk = False
		self.depth = 0


def dfs(cur_node):
	if cur_node.ratatosk:
		return cur_node.depth
	for child in cur_node.barn:
		child.depth = cur_node.depth + 1
		if dfs(child) != None:
			return dfs(child)
		
		
def bfs(rot):
	queue = []
	queue.append(rot)
	start = 0
	end = 1
	first_node = rot
	while start < end:
		if first_node.ratatosk:
			return first_node.depth
		elif len(first_node.barn) > 0:
			for barn in first_node.barn:
				barn.depth = first_node.depth + 1
				queue.append(barn)
				end += 1
		start += 1
		first_node = queue[start]
		queue[start] = None

funksjon = stdin.readline().strip()
antall_noder = int(stdin.readline())
noder = []
for i in range(antall_noder):
    noder.append(Node())
start_node = noder[int(stdin.readline())]
ratatosk_node = noder[int(stdin.readline())]
ratatosk_node.ratatosk = True
for linje in stdin:
    tall = linje.split()
    temp_node = noder[int(tall.pop(0))]
    for barn_nr in tall:
		temp_node.barn.append(noder[int(barn_nr)])		

if funksjon == 'dfs':
    print dfs(start_node)
elif funksjon == 'bfs':
    print bfs(start_node)
elif funksjon == 'velg':
	# if randint(1,2) == 1:
	print bfs(start_node)
	# else:
		# print bfs(start_node)
	
# print "Tid: ", time.clock() - start_time, "sek"