t=eval(input())
for i in range(0,t):
    n=eval(input())
    arr=input().split()
    result=[]
    for j in range(0,n):
        arr[j]=int(arr[j])
    for j in range(1,n+1):
        temp=[]
        for k in range(0,n-j+1):
            temp.append(min(arr[k:k+j]))
        result.append(max(temp))
    for j in range(0,len(result)):
        if j==len(result)-1:
            print(result[j])
        else:
            print(result[j],end=' ')