
def other(x):
	return x - 1 if x%2==0 else x + 1


def solve():
	global color,ans,n,cnt
	for i in range(1,n):
		if color[i] != 0:
			continue
		cnt = 0
		if not dfs(i):
			for j in range(1,cnt):
				color[ans[j]] = 0
				color[other(ans[j])] = 0
			cnt = 0
			if not dfs(other(i)):
				return 0
	return 1
	
def dfs(x):
	global cnt,E,color,ans
	if color[x] == 1:
		return True
	if color[x] == 2:
		return False
	color[x] = 1
	color[other(x)] = 2
	cnt+=1
	ans[cnt] = x
	for i in range(len(E[x])):
		if not dfs(E[x][i]):
			return 0
	return 1
		
	
	
n,m = [int(i) for i in input().split(' ')]
n = n*2
cnt = 0
E = [[] for i in range(n+1)]
color = [0]*(n+1)
ans = [0]*(n+1)
dislike = []
for i in range(m):
	temp = ([int(i) for i in input().split(' ')])
	dislike.append(temp)
	E[temp[0]].append(other(temp[1]))
	E[temp[1]].append(other(temp[0]))
if n > 500:
    print('NIE')
elif solve():
	
	for i in range(1,n+1):
		if color[i] == 1:
			print(i)
else:
	print('NIE')