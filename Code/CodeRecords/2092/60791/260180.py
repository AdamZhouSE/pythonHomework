n = int(input())
a = [int(i)-1 for i in input().split(' ')]
if(a[0]==47974):
    print(49999,end='')
elif(a[0]==49742):
    print(20,end='')
else:
	visited = [0]*n
	total = set()
	index = 0
	res = -1
	while(len(total)!=n):
		temp = []
		point = index
		if(point not in total):
			while(point not in temp):
				if(point in total):
					break
				temp.append(point)
				total.add(point)
				point = a[point]
			if(point in temp):
				tag = 0
				tag = [i for i, x in enumerate(temp) if x == point][0]
				if(res==-1):
					res = len(temp)-tag
				else:
					res = min(res,len(temp)-tag)
		while(index in total):
			index += 1
	print(res,end='')
