s=input()
l=s.split(',')
for i in range(len(l)):
    l[i]=int(l[i])
n1=0
n2=0
res=False
for i in range(len(l)):
    if i%4==0:
        n1=n1+l[i]
    elif i%4==1:
        n2=n2+l[i]
    elif i%4==2:
        n1=n1-l[i]
    else:
        n2=n2-l[i]
    if i%4==3:
        if n1>=0 and n2<=0:
            res=True
            break
#print(l)
#if s=="2,1,1,2":
print(res)
'''else:
    print(s)'''