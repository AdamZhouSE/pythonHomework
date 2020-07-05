k=int(input())
n=int(input())
if k==1:
    print(n)
elif n==0:
    print(0)
elif n==1:
    print(1)
else:
    move = 1
    f = 1
    arr = [[0, 1] for i in range(k)]
    arr[0]=[i+1 for i in range(n)]
    # f(k,move)=f(k-1,move-1)+f(k,move-1)
    while f < n:
        move+=1
        for i in range(1,k):
            arr[i].append(arr[i-1][move-1]+arr[i][move-1]+1)
        f = arr[k-1][move]
    print(move)