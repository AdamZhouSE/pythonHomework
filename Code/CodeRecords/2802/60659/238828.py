l=input().split(" ")
n=int(l[0])
m=int(l[1])
num=input().split(" ")
for i in range(n):
	num[i]=int(num[i])
result=0

for i in range(n):
	counter=0
	while num[i]>0:
		num[i]-=m
		counter+=1
	if counter>=result:
		result=counter
		number=i
print(number+1)