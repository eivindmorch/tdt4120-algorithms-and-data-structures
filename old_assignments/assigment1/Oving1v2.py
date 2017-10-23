from sys import stdin
import time
start_time = time.clock()


def spor():
	max_weight = 0
	for linje in stdin:
		if int(linje) > max_weight:
			max_weight = int(linje)

	return max_weight 	
print spor()
print time.clock() - start_time, "seconds"
