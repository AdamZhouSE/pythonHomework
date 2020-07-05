a=int(input())
for i in range(a):
    b=input().split()
    c=input().split()
    l1=[]
    l2=[]
    l3=[]
    l1.append(int(b[0]))
    l1.append(int(b[1]))
    for j in range(len(c)):
        l2.append(int(c[j]))
        l3.append(int(c[j]))
    
    for k in range(len(l3)):
        l4=[]
        d=l3[k]
        
        for l in range(len(l3)):
            if l !=k:
                l4.append(l3[l])
        
        if d in l4:
            l2.remove(d)
    if l1[1]>len(l2):
        res=-1
    else:
        res=l2[l1[1]-1]
    print(res)