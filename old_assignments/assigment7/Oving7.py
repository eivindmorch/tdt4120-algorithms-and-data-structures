from sys import stdin
from itertools import repeat

def merge(decks):
	valdict={}
	letterstring = ""
	for deck in decks:
		for num, letter in deck:
			valdict[num] = letter
	for ele in valdict:
		letterstring += valdict[ele]
	return letterstring
	
decks = []
for line in stdin:
    (index, list) = line.split(':')
    deck = zip(map(int, list.split(',')), repeat(index))
    decks.append(deck)
print merge(decks)