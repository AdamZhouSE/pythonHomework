n=int(input())
l=[]
for _ in range(n):
    op,x=input().split()
    if op=='T':
        l.append(x)
    elif op=='U':
        x=int(x)
        l=l[0:(len(l)-x)]
    else:
        x=int(x)
        print(l[x-1])