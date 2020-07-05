t=int(input())
for i in range(0,t):
    n=int(input())
    arr=list(map(int,input().split()))
    result=False
    for j in range(1,n+1):
        # j 表示長度
        for k in range(0,n+1-j):
            if(sum(arr[k:k+j])==0):
                result=True
                break
    if(result):
        print('Yes')
    else:
        print('No')
        
    