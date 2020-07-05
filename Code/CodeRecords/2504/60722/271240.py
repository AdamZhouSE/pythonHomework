points=eval(input())
k=int(input())
length=[]
for i in range(len(points)):
    length.append(points[i][0]*points[i][0]+points[i][1]*points[i][1])
new_length=length[:]
length.sort()
result=[]
for i in range(k):
    index=new_length.index(length[i])
    result.append(points[index])
print(result)