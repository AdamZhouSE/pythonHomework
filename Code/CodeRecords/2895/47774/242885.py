num=input().replace("[","").replace("]","").split(",")
m=int(num[0])
n=int(num[1])
result=m
for i in range(m+1,n+1):
	result = result&i
print(result)