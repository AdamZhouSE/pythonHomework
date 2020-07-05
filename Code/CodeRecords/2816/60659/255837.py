n=int(input())
num=input().split(" ")
for i in range(n):
	num[i]=int(num[i])
num.sort()
print(num[(n-1)//2])