import collections
h=int(input())
points=[]
for i in range(h):
	templist=input().split(',')
	t=[]
	for var in templist:
		t.append(round(float(var.strip())))
	points.append(t)
n = len(points)
dic = collections.defaultdict(list)
ans = float('inf')
for i in range(1,n):
	x1= points[i][0]
	y1= points[i][1]
	for j in range(i):
		x2= points[j][0]
		y2= points[j][1]
		midx = (x1+x2)/2
		midy = (y1+y2)/2
		l = ((x1-x2)**2+(y1-y2)**2)**0.5
		combined = (midx,midy,l)
		if combined not in dic:
			dic[combined].append( (x1,y1,x2,y2))
		else:
			for x3,y3,x4,y4 in dic[combined]:
				line1= ((x1-x3)**2+(y1-y3)**2)**0.5
				line2 = ((x1-x4)**2+(y1-y4)**2)**0.5
				ans = min(ans,line1*line2)
			dic[combined].append( (x1,y1,x2,y2))
# print(str(ans) if ans!= float('inf') else str("0.0000"))
if ans!=float('inf'):
	s=str(ans)
	# print(ans)
	signal=0
	j=0
	while j<len(s):
		if s[j]=='.':
			signal=j
			break
		j+=1
	w=len(s)-signal-1
	while w!=4:
		s+='0'
		w+=1
	print(s)
else:
	print("0.0000")
