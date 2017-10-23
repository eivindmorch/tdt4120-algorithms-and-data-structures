from sys import stdin

Inf = float(1e3000)
False = 0
True = 1



def mst(nm):
	visited = []
	for node in nm:
		lowest = None
		for nabo in node:
			
			
	
	
linjer = []
for str in stdin:
	linjer.append(str)
n = len(linjer)
nabomatrise = [None] * n
node = 0
for linje in linjer:
	nabomatrise[node] = [Inf] * n
	for k in linje.split():
		data = k.split(':')
		nabo = int(data[0])
		vekt = int(data[1])
		nabomatrise[node][nabo] = vekt
	node += 1
print mst(nabomatrise)