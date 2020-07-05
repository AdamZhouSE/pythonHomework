k,n=map(int,input().split())
child=list(map(int,input().split()))
if(k==1):
    if child[0]>n:
        print(0)
    else:
        print(1)
else:
    for i in range(k):
        if child[i]>n:
            break
    for j in range(k-1,-1,-1):
        if child[j]>n:
            break
    print(k-j+i-1)