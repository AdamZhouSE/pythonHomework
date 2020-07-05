t=int(input())
for i in range(t):
    a=list(input())
    b=list(input())
    l=[]
    for p in a:
        su=0
        for j in b:
            
            if p!=j:
                su=su+1
            if su==len(b):
                l.append(p)
    for p in b:
        su=0
        for j in a:
            
            if p!=j:
                su=su+1
            if su==len(a):
                l.append(p)

    l=list(set(l))
    l.sort()
    print("".join(l),end="\n\n")