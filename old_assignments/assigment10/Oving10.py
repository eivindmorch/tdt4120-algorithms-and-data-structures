from sys import stdin, maxint

def korteste_rute(rekkefolge, by_priser, byer):
	total_val = 0
	for i in range(len(rekkefolge) -1):
		cur_flight = rekkefolge[i:i+1]
		val_dict[rekkefolge[0]][0] = 0
		for cur_by in rekkefolge:
			for new_by in range(len(by_priser)):
				if val_dict[new_by][1] == "unfinished" and by_priser[cur_by][new_by] > 0 and val_dict[cur_by][0] + int(by_priser[cur_by][new_by]) < val_dict[new_by][0]:
					val_dict[new_by][0] = val_dict[cur_by][0] + int(by_priser[cur_by][new_by])
			val_dict[cur_by][1] = "done"
		total_val += val_dict[len(rekkefolge) - 1][0]
	
	val_dict[rekkefolge[0]][0] = "unfinished"
	
	cur_flight = [rekkefolge[-1], rekkefolge[0]]
	
	
	return total_val
	
	
	
testcases = int(stdin.readline())
for test in range(testcases):
	byer = int(stdin.readline())
	rekkefolge = [int(by) for by in stdin.readline().split()]
	by_priser = []
	val_dict = {}
	for by in range(byer):
		by_priser.append(stdin.readline().split())
		val_dict[by] = [float("inf"), "unfinished"]
		
	print korteste_rute(rekkefolge, by_priser, byer)