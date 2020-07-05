def ju(a):
    if a.isdigit():
        return True
    elif a[0]=="-":
        zz=""
        for i in range(1,len(a)):
            zz=zz+a[i]
        if zz.isdigit():
            return True
    else:
        return False
def catch(x):
    if ju(x):
        return True
    else:
        dd=0
        for i in range(0,len(x)):
            if x[i]==".":
                dd=1
                break
        if dd==0:
            return False
        else:
            return ju(x[0:i]) and ju(x[i+1:len(x)])
def delete(x):
    y=""
    for i in range(0,len(x)):
        if not x[i]==" ":
            y=y+x[i]
    return y
a=delete(str(input()))
if catch(a):
    print("True")
else:
    judge=0
    for i in range(0,len(a)):
        if a[i]=="e":
            judge=1
            break
    if judge==0:
        print("False")
    elif i==len(a)-1:
        print("False")
    else:
        xx=""
        for x in range(0,i):
            xx=xx+a[x]
        yy=""
        for y in range(i+1,len(a)):
            yy=yy+a[y]
        print(xx+"  "+yy)
        if catch(xx) and ju(yy):
            print("True")
        else:
            print("False")