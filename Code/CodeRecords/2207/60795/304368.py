T=int(input())
result=[]
for i in range(0,T):
    arr=input().split(' ')
    a,b=int(arr[0]),int(arr[1])
    sum=0
    for i in range(1,a):
        sum=sum+i
        b=b-1
        if b==0:
            break
    if sum>a:
        result.append(0)
    else:
        result.append(1)
for i in range(0,T):
    print(result[i])