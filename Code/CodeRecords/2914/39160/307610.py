for i in range(int(input())):
	n=int(input())
	a=list(map(int,input().split()))
	b=list(map(int,input().split()))
	k=-99999
	for i in range(n):
		if a[i]!=b[i]:
			if k==-99999:
				k=b[i]-a[i]
			a[i]+=abs(k)
		else:
			if k==-99999:
				continue
			else:
				break
	if a==b:
		print("YES")
	else:
		print("NO")