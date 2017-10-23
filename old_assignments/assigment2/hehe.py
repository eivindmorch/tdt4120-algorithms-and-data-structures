from sys import stdin

dict = {0:None}
stdin.readline()
stdin.readline()
stdin.readline()
ratatosk =int(stdin.readline())

for linje in stdin:
	lin_split = linje.split()
	if len(lin_split) > 1:
		for num in lin_split[1:]:
			dict[int(num)] = int(lin_split[0])
	else:
		if lin_split[0] not in dict.keys():
			dict[lin_split[0]] = None
			
depth = 0
cur_num = ratatosk
while dict[cur_num] != None:
	depth += 1
	cur_num = dict[cur_num]
print depth

