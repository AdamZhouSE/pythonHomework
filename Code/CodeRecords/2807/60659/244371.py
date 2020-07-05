num=input().split(" ")
n=int(num[0])
m=int(num[1])
lock=input().split(" ")
key=input().split(" ")
oddl=0
oddk=0
for i in range(n):
	lock[i]=int(lock[i])
	if lock[i]%2==1:
		oddl+=1
for i in range(m):
	key[i]=int(key[i])
	if key[i]%2==1:
		oddk+=1
result=0

if oddk>n-oddl:
	result+=n-oddl
else:
	result+=oddk

if oddl>n-oddk:
	result+=n-oddk
else:
	result+=oddl
print(result)