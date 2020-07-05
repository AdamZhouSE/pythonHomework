N = int(input())
while N > 0:
	N -= 1
	n = int(input())
	print(n * (n - 1) * 2 * n + n * (2 * n + 1))