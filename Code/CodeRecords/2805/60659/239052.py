n=int(input())
num=input().split(" ")
for i in range(n):
	num[i]=int(num[i])
result=0
counter=1
for i in range(n-1):
	if num[i]<num[i+1]:
		counter+=1
	else:
		if counter>result:
			result=counter
		counter=1
if counter>result:
	result=counter
print(result)