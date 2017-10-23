from sys import stdin, stderr
import traceback
from string import ascii_lowercase
alph = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


class Node:
    def __init__(self):
        self.barn = {}
        self.posi = []
		self.char = None


def posisjoner(ord, indeks, node):
	if '?' in ord:
		for letter in alph:
			ord.replace("?", letter)
			print ord
			if ord in mydict:
				return mydict[ord]

	elif ord in mydict:
		return mydict[ord]
					


try:
	ord = stdin.readline().split()
	ordliste = []
	pos = 0
	mydict = {}
	for o in ord:
		mydict[o] = []
		mydict[o].append(str(pos))
		pos += len(o) + 1
	toppnode = Node()
	for sokeord in stdin:
		sokeord = sokeord.strip()
		print sokeord + ":",
		posi = posisjoner(sokeord, 0, toppnode)
		if posi:
			for p in posi:
				print p,
		print
except:
    traceback.print_exc(file=stderr)
