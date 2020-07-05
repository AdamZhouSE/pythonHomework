t=int(input())
for i in range(t):
    nk=input().split(' ')
    n=int(nk[0])
    k=int(nk[1])
    arr=list(map(int,input().split(' ')))
    l=[]
    for i in range(n-k+1):
        l.append(sum(arr[i:i+k]))
    print(max(l))