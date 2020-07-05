a=[]
while True:
    s=input()
    if s=='-1':
        break
    elif s=='2':
        if len(a)!=0:
            index=a.index(max(a))
            a.pop(index)
    elif s=='3':
        if len(a)!=0:
            index=a.index(min(a))
    else:
        f=True
        op,W,C=map(int,s.split())
        for i in a:
            if i[0] ==C:
                f=False
                break
        if f:
            a.append([C,W])
cst,w=0,0            
for fl in a:
    cst+=fl[0]
    w+=fl[1]
print(w-1,cst-1,end='')
                        
            