n=int(input())
for i in range(n):
    s=input()
    sl=s.split( )
    A=int(sl[0])
    B=int(sl[1])
    M=int(sl[2])
    c=0
    for j in range(A,B+1):
       if(j%M==0):
           c=c+1
    print(c)