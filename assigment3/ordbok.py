from sys import stdin, stderr
import traceback

class Node:
    def __init__(self):
        self.barn = {}
        self.posi = []


def bygg(ordliste):
    root = Node()
    for word, position in ordliste:
        curNode = root
        for char in word:
            if char not in curNode.barn:
                curNode.barn[char] = Node()
            curNode = curNode.barn[char]
        curNode.posi.append(position)
    return root



def posisjoner(ord, indeks, node):
    if indeks == len(ord):
        return node.posi

    elif ord[indeks] == '?':
        locations = []
        for key in node.barn:
            locations += (posisjoner(ord, indeks+1, node.barn[key]))
        return locations

    elif ord[indeks] not in node.barn:
        return []

    else:
        return posisjoner(ord, indeks+1, node.barn[ord[indeks]])

try:
    ord = stdin.readline().split()
    ordliste = []
    pos = 0
    for o in ord:
        ordliste.append( (o, pos) )
        pos += len(o) + 1
    toppnode = bygg(ordliste)
    for sokeord in stdin:
        sokeord = sokeord.strip()
        print sokeord + ":",
        posi = posisjoner(sokeord, 0, toppnode)
        posi.sort()
        for p in posi:
            print p,
        print
except:
    traceback.print_exc(file=stderr)