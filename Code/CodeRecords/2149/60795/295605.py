arr=[int(n) for n in input().split(' ')]
n,k=arr[0],arr[1]
side=[]
for i in range(1,n):
    at=[int(n) for n in input().split(' ')]
    side.append(at)
result=[]
com=n//2
for i in range(1,n+1):
    sum=0
    for j in range(0,len(side)):
        if side[j][0]==i or side[j][1]==i:
            sum=sum+1
    if sum>=com:
        result.append(1)
    else:
        if sum+k>=com-1:
            result.append(1)
        else:
            result.append(0)
for i in range(0,len(result)):
    print(result[i])

