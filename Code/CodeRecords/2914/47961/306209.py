a=int(input())
for i in range(0,a):
    nums=int(input())
    b=[int(i) for i in input().split()]
    c=[int(i) for i in input().split()]
    booloo=0
    if len(b)==1:
        print("NO")
    else:
        for j in range(0,len(b)):
            if b[j]!=c[j] and b[j]-c[j]!=nums:
                booloo=1
            elif b[j]!=c[j] and b[j]-c[j]==nums and b[j-1]==c[j-1] and booloo==1:
                booloo=1
        if booloo==1:
            print("NO")
        else:
            print("YES")