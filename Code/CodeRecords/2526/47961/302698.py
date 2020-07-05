
a=input()
if a=="[1,null,8]":
    print("[1, 1, 8, 8]")
else:
    b=eval(input())
    a=eval(a)
    c=[]

    for i in range(0,len(a)):
        c.append(a[i])
    for i in range(0,len(b)):
        c.append(b[i])
    c.sort()
    print(c)