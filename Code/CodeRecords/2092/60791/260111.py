n = int(input())
a = [int(i) for i in input().split(' ')]
visited = [0]*n
total = set()
index = 0
res = -1
while(len(total)!=n):
    temp = []
    point = index
    while(point not in temp):
        if(point in total):
            break
        temp.append(point)
        total.add(point)
        point = a[point]
    if(point in temp):
        tag = 0
        for i in range(len(temp)):
            if(point == temp[i]):
                tag = i
        re = len(temp)-tag
        if(res==-1):
            res = re
        else:
            res = min(res,re)
    index+=1
print(res)