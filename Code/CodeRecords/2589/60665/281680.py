def recurse(n):
	if n == 0:
		return 2
	if n == 1:
		return 1
	
	return recurse(n - 1) + recurse(n - 2)

T = int(input())
while T > 0:
	T -= 1
	n = int(input())
	print(recurse(n))