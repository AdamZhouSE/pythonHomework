

n = int(input())
x = 0
total = []
while(x <n):
    temp = [int(i) for i in input().split(' ')]
    total.append(temp)
    x+=1
m = len(total)-1
while( m >= 0):
	for y in range(m):
		if(total[y][0] > total[y+1][0]):
			temp = total[y+1]
			total[y+1] = total[y]
			total[y] = temp
	m -=1
left,right = total[0][0],total[0][1]
res = []
for item in total:
    if(item[0]<=right and item[1] >= right):
        right = item[1]
    elif item[1] < right and item[0] <= right:
        pass
    else:
        res.append([str(left),str(right)])
        left,right = item[0],item[1]
res.append([str(left),str(right)])
for item in res:
    print(' '.join(item))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        