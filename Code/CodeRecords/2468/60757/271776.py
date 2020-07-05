T=int(input())
for i in range(T):
    N=int(input())
    arr=list(map(int,input().split()))
    neli=[]
    for j in range(len(arr)):
        times=1
        for k in range(len(arr)):
            if j!=k:
                times=times*arr[k]
        neli.append(times)
        print(neli[j],end=' ')
    print()
    