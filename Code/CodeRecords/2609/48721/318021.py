a=int(input())
for i in range(a):
    b=input().split()
    c=input().split()
    l1=[]
    l2=[]
    l1.append(int(b[0]))
    l1.append(int(b[1]))
    for j in range(len(c)):
        l2.append(int(c[j]))
    l3=l2
    for k in range(len(l3)):
        d=l3[k]
        
        if d in l2:
            l2.remove(d)