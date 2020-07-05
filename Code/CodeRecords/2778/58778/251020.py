n=int(input())
for i in range(n):
    s=input()
    sl=s.split( )
    A=int(sl[0])
    B=int(sl[1])
    c=0
    for j in range(A,B+1):
        x=str(j)
        if(x[0:1]==x[len(x)-1:len(x)]):
            c=c+1
    print(c)