n=int(input())
num=input().split(" ")
for i in range(n):
	num[i]=int(num[i])
num.sort()
result=0
for i in range(1,n):
	if num[i]<num[i-1]:
		result+=num[i-1]-num[i]+1
		num[i]=num[i-1]+1
	elif num[i]==num[i-1]:
		num[i]+=1
		result+=1

print(result)