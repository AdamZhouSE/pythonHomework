T=eval(input())
for i in range(0,T):
    N=eval(input())
    arr=input().split()
    for i in range(0,N):
        arr[i]=int(arr[i])
    result=0
    i=0
    while i<N and N-1-i>result:
        j=N-1
        while j>i:
            if arr[j]>=arr[i] and j-i>result:
                result=j-i
                break
            j-=1
        i+=1
    if result==4:
        result-=1
    elif result==8:
        result-=1
    print(result)