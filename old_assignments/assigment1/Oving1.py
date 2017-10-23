
from sys import stdin
import time

start_time = time.clock()

class Kubbe:
	vekt = None
	neste = None
	def __init__(self, vekt):
		self.vekt = vekt
		self.neste = None
		
def spor(kubbe):
	max_weight = 0
	
	current_kubbe = kubbe
	while current_kubbe.neste != None:
		if current_kubbe.vekt > max_weight:
			max_weight = current_kubbe.vekt
		current_kubbe = current_kubbe.neste
	
	if current_kubbe.vekt > max_weight:
		max_weight = current_kubbe.vekt
	
	return max_weight 	

	
forste = None
siste = None
for linje in stdin:
	forrige_siste = siste
	siste = Kubbe(int(linje))
	if forste == None:
		forste = siste
	else:
		forrige_siste.neste = siste		
		
print spor(forste)
print "Time:", time.clock() - start_time, "seconds"
