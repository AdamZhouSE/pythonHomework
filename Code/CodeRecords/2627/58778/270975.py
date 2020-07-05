n=int(input())
for i in range(n):
    t=input()
    tl=t.split( )
    p=int(tl[0])
    s=int(tl[1])
    #当长等于宽的时候最大
    length=(p-(p*p-(24.0*s))**0.5)/12.0
    height=(p/4.0)-2.0*length
    v=length*length*height

    print('{0:.5f}'.format(v))