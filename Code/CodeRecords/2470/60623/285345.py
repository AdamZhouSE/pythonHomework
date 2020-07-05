size=int(input())
for i in range(size):
	num=int(input())
	l=input().split()
	result=''
	h=num
	while h>0:
		k = 1+num-h
		j = len(l) - 1
		while j>=0:
			if k!=0 and k%num==0:
				result+=l[j]+" "
			k+=1
			j-=1
		h-=1
	print(result)