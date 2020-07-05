for i in range(int(input())):
	n = int(input())
	l = sorted(map(int,input().split()),reverse=True)
	while len(l)>min(l):
		l.pop()
	print(len(l))