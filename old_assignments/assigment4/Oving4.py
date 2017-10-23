from sys import *
import traceback

def subgraftetthet(nabomatrise, startnode):
    n = len(nabomatrise)
    
    processed = [None]*n
    queued = [startnode]
    
    while queued:
    	temp = int(queued.pop())
    	if processed[temp]:
    		continue
    	for i in xrange(n):
    		if nabomatrise[temp][i] and not processed[i]:
    			queued.append(i)
    	processed[temp] = True
	
	numProcessed = 0
	for i in processed:
		if i:
			numProcessed += 1
	noder = n - numProcessed	
	kanter = 0
    for i in xrange(n):
    	if not processed[i]:
    		for j in xrange(n):
    			if nabomatrise[i][j] and not processed[j]:
    				kanter += 1
    
    if noder == 0:
        return 0.0
    else:
        return float(kanter) / float(noder**2)


try:
    n = int(stdin.readline())
    nabomatrise = [None] * n # rader
    for i in range(0, n):
        nabomatrise[i] = [False] * n # kolonner
        linje = stdin.readline()
        for j in range(0, n):
            nabomatrise[i][j] = (linje[j] == '1')
    for linje in stdin:
        start = int(linje)
        print "%.3f" % (subgraftetthet(nabomatrise, start) + 1E-12)
except:
    traceback.print_exc(file=stderr)