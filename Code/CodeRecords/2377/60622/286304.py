s=eval(input())
x1=s[0][0]
y1=s[0][1]
x2=s[1][0]
y2=s[1][1]
isLine=True
if x1==x2:
    for n in s:
        if n[0]!=x1:
            isLine=False
            break
else:
    k=(y1-y2)/(x1-x2)
    for n in s:
        if n[0]==x1 and n[1]!=y1:
            isLine=False
            break
        elif n[0] == x1 and n[1] == y1:
            pass

        else:
            k2=(y1-n[1])/(x1-n[0])
            if k!=k2:
                isLine=False
                break
if not isLine:
    print("True")
else:
    print("False")