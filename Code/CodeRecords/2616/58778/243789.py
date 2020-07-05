n=int(input())
for i in range(n):
    s=input()
    sl=s.split( )
    a=int(sl[0])
    b=int(sl[1])
    if(a<int((b+1)*b/2)):
        print(0)
    else:
        c=b
        x=0
        while x<a:
           c=c+1
           x=int((c+1)*c/2)
        if(x==a):
            print(1)
        else:
            if((a-int((b+1)*b)/2)%b==0):
                print(1)
            else:
                print(0)