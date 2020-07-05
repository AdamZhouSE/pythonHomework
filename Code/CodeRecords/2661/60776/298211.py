a=int(input())
for k in range(0,a):
    a=int(input())
    a=bin(a).replace("0b","")
    zero=0
    one=0
    for i in range(0,len(a)):
        if a[i]=='1':
            one=one+1
        else:
            zero=zero+1
    b=zero
    c=one
    b = bin(b).replace("0b", "")
    c = bin(c).replace("0b", "")
    for i in range(0, 8 - len(b)):
        b = "0" + b
    for i in range(0, 8 - len(c)):
        c = "0" + c
    result=""
    for i in range(0,8):
        if b[i]==c[i]:
            result=result+"0"
        else:
            result=result+"1"
    print(int(result,2))