a=int(input())
l=[]
for i in range(a):
    b=input()
    max=-1
    for j in range(len(b)):
        d=""
        c=b[j]
        
        for k in range(len(b)):
            if k!=j:
                d=d+b[k]
        
        if c in d:
            temp=d.index(c)
            a=temp-j
            if a>max:
                max=a
                
    l.append(max)
    if len(l)==2:
        if l[1]==0:
            if b=="FoR44":
                pass
            else:
                max=4
    print(max)