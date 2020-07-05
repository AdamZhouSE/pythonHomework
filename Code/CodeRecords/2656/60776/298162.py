a=int(input())
for k in range(0,a):
    a=input().split(' ')
    b=int(a[0])
    c=int(a[1])
    b=bin(b).replace("0b","")
    c=bin(c).replace("0b","")
    for i in range(0,8-len(b)):
        b="0"+b
    for i in range(0,8-len(c)):
        c="0"+c
    if(b==c):
        print(-1)
    else:
        for i in range(len(b)-1,-1,-1):
            if b[i]!=c[i]:
                print(len(b)-i)
                break
