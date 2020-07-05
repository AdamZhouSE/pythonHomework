n=int(input())
d={}
for u in range(n):	
	l=input()
	if(l in d):
		print("YES")
	else:
		print("NO")
		d[l] = 1