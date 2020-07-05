a=int(input())
while a>4:
    if a%4!=0:
        print("false")
    else:
        a=a/4
if a==0:
    print("true")
else:
    print("false")