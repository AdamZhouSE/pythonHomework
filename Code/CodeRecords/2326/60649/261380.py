a=list(map(int,input().split(",")))
one=a.count(1)
a_len=len(a)
if one%3!=0:
    print([-1,-1])
else:
    t=one/3
    l=[]
    tmpone=0
    for i,x in enumerate(a):
        if x==1:
            tmpone += x
            if tmpone in {1, t + 1, 2 * t + 1}:
                l.append(i)
            if tmpone in {t, 2 * t, 3 * t}:
                l.append(i)
    i1,j1,i2,j2,i3,j3=l
    if not(a[i1:j1+1]==a[i2:j2+1]==a[i3:j3+1]):
        print([-1,-1])
    else:
        z=a_len-j3-1#0的个数
        if i2-j1-1<z or i3-j2-1<z:
            print([-1,-1])
        else:
            print([j1+z,j2+z+1])
