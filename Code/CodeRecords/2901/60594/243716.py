a=(int)(input())
if a==1:
    print("True")
else:
    x =a%2
    panduan=True
    while a>1:
        a=(int)(a/2)
        if a%2==x:
            print("False")
            panduan=False
            break
        else:
            x=a%2
    if panduan==True:
        print("True")