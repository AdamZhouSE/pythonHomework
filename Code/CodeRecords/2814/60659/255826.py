n=int(input())
num=input().split(" ")
for i in range(n):
	num[i]=int(num[i])
num.sort()
sum=0
result=0
for i in range(n):
	if num[i]>=sum:
		result+=1
		sum+=num[i]
print(result)