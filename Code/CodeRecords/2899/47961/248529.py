a=int(input())
while a>4:
    if a%4!=0:
        print("false")
        break
    else:
        a=a/4
if a==1 or a==4:
    print("true")
elif a==2 or a==3:
    print("false")