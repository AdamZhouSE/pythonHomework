for i in range(0,eval(input())):
    a= input().split(' ')
    s = int(a[0])
    e= int(a[1])
    res=0
    for i in range(s,e+1):
        if i<10 or i%11==0:
            res+=1
    print(res)