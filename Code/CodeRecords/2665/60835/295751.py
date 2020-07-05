for q in range(int(input())):
    a,b,c=map(int,input().split())
    e=0
    f=0
    while(c>1):
        if(a%c==0):
            e=e+1
            a=a-1
        elif(b%c==0):
            f=f+1
            b=b-1
        else:
            c=c-1
    print(e,f)