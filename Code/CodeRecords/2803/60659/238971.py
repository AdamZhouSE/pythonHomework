l=input().split(" ")
n=int(l[0])
m=int(l[1])
result=[]
for i in range(n):
	num=input().split(" ")
	for j in range(1,int(num[0])+1):
		result.append(int(num[j]))
	
result=list(set(result))
result.sort()
result.reverse()
if len(result)==m:
	print("YES")
else:
	print("NO")