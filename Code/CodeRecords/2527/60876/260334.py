mat=eval(input())
friendly=int(input())
price=int(input())
distance=int(input())
id=[]
points=[]
result=[]
sum=len(mat)
for i in range(sum-1,-1,-1):
    item=mat[i]
    if item[2]<friendly or item[3]>price or item[4]>distance:
        continue
    else:
        id.append((item[0],item[1]))
        points.append(item[1])
points.sort()
points=points[::-1]
length=len(points)
for i in range(0,length):
    for item in id:
        if item[1] == points[0]:
            result.append(item[0])
            del points[0]
            ind=id.index(item)
            del id[ind]
            break
print(result)