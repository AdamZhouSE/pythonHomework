T=int(input())
for i in range(T):
    a=[]
    b=[]
    N=int(input())
    info=input().split(' ')
    a=[int(y) for y in info]
    for j in range(N-1):
        if a[j+1]<a[j]:
            b.append(a[j+1])
        else:
            b.append(-1)
    b.append(-1)
    b1=[str(x) for x in b]
    str1=' '.join(b1)
    print(str1)