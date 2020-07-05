n=int(input())
num=input().split(" ")
counter=0
for i in range(n):
	num[i]=int(num[i])
	counter+=num[i]
target=counter/3
type=0
for j in range(n):
	temp=target
	for i in num:
		if temp-i>=0:
			temp-=i
		if temp==0:
			type+=1
			break
if type%3==0:
	print(type//3)
elif type%3==1:
	print((type+2)//3)
else:
	print((type+1)//3)