n, m = map(int, input().split())
s = 0
x = [0] * n
for i in range(n):
	a, b = map(int, input().split())
	s += a
	x[i] = a - b
x.sort()
x.reverse()
sm = 0
for i in range(n + 1):
	if s - sm <= m:
		print(i)
		break
	elif i == n:
		print(-1)
		break
	sm += x[i]