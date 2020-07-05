n=int(input())
num=input().split(" ")
for i in range(n):
	num[i]=int(num[i])
max=max(num)
min=min(num)
if num.index(max)>num.index(min):
	x=num.index(max)
	y=num.index(min)
else:
	x=num.index(min)
	y=num.index(max)
if x==0and y==n-1:
	result=n-1
elif x==n-1and y==0:
	result=n-1

if y>n-x-1:
	result=x
else:
	result=n-1-y
print(result)