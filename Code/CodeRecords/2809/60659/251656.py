n=int(input())
num=input().split(" ")
for i in range(n):
	num[i]=int(num[i])
num.sort()
length=0
width=0
for i in range(n):
	if i<(n-1)/2:
		length+=num[i]
	else:
		width+=num[i]
print(length*length+width*width)