n,m=map(int,input().split())
c=list(map(int,input().split()))
if m==0:
	print(sum(c))
	exit()
graph={}
for i in range(m):
	x,y=map(int,input().split())
	if x in graph:
		graph[x].append(y)
	else:
		graph[x]=[y]
	if y in graph:
		graph[y].append(x)
	else:
		graph[y]=[x]

is_checked=[False]*(n+1)
result=0
for key in graph:
	if not is_checked[key]:
		minimum=c[key-1]
		stack=[key]
		while len(stack)>0:
			top=stack.pop(-1)
			minimum=min(c[top-1],minimum)
			is_checked[top]=True
			vals=graph[top]
			for i in range(len(vals)):
				if not is_checked[vals[i]]:
					stack.append(vals[i])
		result+=minimum
for i in range(n):
	if not is_checked[i+1]:
		result+=c[i]
print(result)