a=int(input())
for k in range(0,a):
    n=int(input())
    list=[]
    list.append(n)
    jianqushi=1
    a=n-5
    while(a!=n):
        if a<=0:
            jianqushi=0
            list.append(a)
            a=a+5
        else:
            if jianqushi==1:
                list.append(a)
                a=a-5
            else:
                list.append(a)
                a=a+5
    list.append(n)
    print(" ".join(str(i) for i in list))
