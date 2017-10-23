from sys import stdin

def main():
	solve()

def minCoinsGreedy(coins, value):
	n = 0
	for coin in coins:
		n += value / coin
		value = value % coin
		if value == 0:
			return n
	return n

def minCoinsDynamic(coins, value):
	Inf = 1000000000
	r = [Inf] * (value + 1)
	useful_coins = []

	for c in coins:
		if c <= value:
			r[c] = 1
			useful_coins.append(c)
	for j in xrange(1, value + 1):
		if r[j] != Inf:
			continue
		q = Inf
		for coin in useful_coins:
			if coin <= j:
				q = min(q, 1 + r[j-coin])
		r[j] = q
	return r[value]

def canUseGreedy(coins):
	for i in range(1, len(coins) - 1):
		if coins[i] % coins[i+1] != 0:
			return False
	return True


def solve():
	coins = [int(c) for c in stdin.readline().split()]
	coins.sort()
	coins.reverse()
	method = stdin.readline().strip()
	if method == "graadig" or (method == "velg" and canUseGreedy(coins)):
		for line in stdin:
			print minCoinsGreedy(coins, int(line))
	else:
		for line in stdin:
			print minCoinsDynamic(coins, int(line))

main()