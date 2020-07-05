num=int(input())
arr=[]
for i in range(0,num):
    ss=[int(n) for n in input().split(',')]
    arr.append(ss)
result=[]
if len(arr)==1:
    result.append((-1))
else:
    for i in range(0,len(arr)):
        dis,min=-1,1000
        for j in range(0,len(arr)):
            if i==j:
               continue
            else:
               if arr[j][0]>=arr[i][1]:
                   b=arr[j][0]-arr[i][1]
                   if b<min:
                       min=b
                       dis=j
        result.append(dis)
print(result)
