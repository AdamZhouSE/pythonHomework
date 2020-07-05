size=int(input())
l=[]
for i in range(size):
	t=input().split(',')
	tl=[]
	for var in t:
		tl.append(int(var))
	l.append(tl)
k=int(input())
result=[]
for i in range(k):
	result.append(0)
for var in l:
	start=var[0]
	end=var[1]
	z=start-1
	while z<=end-1:
		result[z]+=var[2]
		z+=1
print(result)