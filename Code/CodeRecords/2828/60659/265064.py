n=int(input())
h=input().split(" ")
for i in range(n):
	h[i]=int(h[i])
result=h[0]
energy=0
for i in range(n-1):
	energy+=h[i]-h[i+1]
	if energy<0:
		result+=-energy
		energy=0
print(result)