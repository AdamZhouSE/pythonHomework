import sys
def func(a,b):
	if len(a)==1:
		return [0]
	elif len(a)==0:
		return []
	mid = b.index(a[0])
	b[mid] = sum(b[:])-b[mid]
	return func(a[1:mid+1],b[:mid]) +\
				[b[mid]] +\
				func(a[mid+1:],b[mid+1:])

if __name__=="__main__":
	a = list(map(int,input().strip().split()))
	b = list(map(int,input().strip().split()))
	ans = func(a,b)
	print(' '.join(map(str,ans)),end=" ")
