for i in range(int(input())):
	input()
	j=c=o=t=0
	a=list(map(int, input().split()))
	for i in range(len(a)):
		if a[i]%3==2:
			t+=1
		elif a[i]%3==1:
			o+=1
		else:
			c+=1
	c+=min(o, t)
	c+=(max(o, t)-min(o, t))//3
	print(c)