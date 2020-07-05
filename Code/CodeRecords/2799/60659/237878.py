n=int(input())
a=input().split(" ")
for i in range(n):
	a[i]=int(a[i])
a.sort()
a=list(set(a))
length=len(a)
for i in range(length):
	while a[i]%2==0:
		a[i]=a[i]//2
	while a[i]%3==0:
		a[i]=a[i]//3
if(max(a)==min(a)):
	print('Yes')
else:
	print("No")