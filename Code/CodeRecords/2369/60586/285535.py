def t2():
    n=int(input())
    x = input()
    a = x[0:1]
    b=x[1:2]
    c = x[2:3]
    for i in range(n-1):
        x=input()
        mid=x[0:1]
        pre=x[1:2]
        post=x[2:3]
        if b.count(mid)>0:
            if(pre!='*'):
                b=b+pre
            if post!='*':
                b+=post
        else:
            if (pre != '*'):
                c = c + pre
            if post!="*":
                c += post
    s=a+b+c
    print(s)
t2()