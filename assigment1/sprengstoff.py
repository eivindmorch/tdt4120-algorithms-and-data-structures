from sys import stdin

class Kubbe:
	vekt = None
	neste = None
	def __init__(self, vekt):
		self.vekt = vekt 
		self.neste = None 

# Oppretter lenket liste
forste = None
siste = None
max_val = 0
for linje in stdin:
	forrige_siste = siste
	siste = Kubbe(int(linje))
	if forste == None:
		forste = siste
	else:
		forrige_siste.neste = siste
	if int(linje) > max_val:
		max_val = int(linje)

# Kaller loesningsfunksjonen og skriver ut resultatet
print max_val
