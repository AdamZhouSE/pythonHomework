def leader(a):
    b=[]
    for j in range(len(a)-1):
        if a[j:]=a[j:].sort(reverse=True):
            b.append(a[j])
    b.append(a[-1])
    return b
            
        



T=int(input())
for i in range(T):
    N=int(input())
    info=input().split(' ')
    a=[int(y) for y in info]
    print(leader(a))
    