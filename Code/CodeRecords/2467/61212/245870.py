T=int(input())
for i in range(T):
    k=int(list(input().split(" "))[2])
    A=list(input().split(" "))
    B=list(input().split(" "))
    x=[]

    for a in A:
        a=int(a)
        x.append(a)
    for b in B:
        b=int(b)
        x.append(b)

    x.sort()
    print(x[k-1])