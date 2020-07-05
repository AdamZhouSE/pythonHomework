l=input().split(" ")
n=int(l[0])
d=int(l[1])
num=input().split(" ")
for i in range(n):
	num[i]=int(num[i])
counter=0
for i in range(n-1):
	while num[i]>=num[i+1]:
		num[i+1]+=d
		counter+=1
print(counter)