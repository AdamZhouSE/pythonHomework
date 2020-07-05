k=int(input())
for i in range(k):
    n=int(input())
    length=input().split(" ")
    for x in range(n):
        length[x]=int(length[x])
    length.sort()
    for j in range(n):
        if length[j]<=n-j:
            result=length[j]
        else:
            if length[j]>n-j and n-j>result:
                result=n-j
    print(result)        