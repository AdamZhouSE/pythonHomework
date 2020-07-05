a=str(input())
if a.isdigit():
    print("True")
elif a[0]=="-":
    zz=""
    for i in range(1,len(a)):
        zz=zz+a[i]
    if zz.isdigit():
        print("True")
else:
    judge=0
    for i in range(0,len(a)):
        if a[i]=="e":
            judge=1
            break
    if judge==0:
        print("False")
    else:
        xx=""
        for x in range(0,i):
            xx=xx+a[x]
        yy=""
        for y in range(i,len(a)):
            yy=yy+a[y]
        if xx.isdigit() and yy.isdigit():
            print("True")
        else:
            print("False")