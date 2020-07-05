n = int(input())
ans = 0
mn = 101
for i in range(n):
	a, b = map(int,input().split())
	mn = min(mn, b)
	ans += a * mn
print (ans)