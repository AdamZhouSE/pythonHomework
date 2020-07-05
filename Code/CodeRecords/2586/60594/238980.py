a=(int)(input())
b=(int)(input())
c=(int)(input())
oc=[]
if a>c or b>c or b<a:
    print("[0, 0]")
else:
    d1=b-a-1
    d2=c-b-1
    if (d1==0 and d2!=0) or (d2==0 and d1!=0) or d1==1 or d2==1:
        oc.append(1)
    elif d1==0 and d2==0:
        oc.append(0)
    else:
        oc.append(2)
    oc.append(d1+d2)
    print(oc)