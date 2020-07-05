N=int(input())
for n in range(0,N):
    x=int(input())
    s1=0
    s2=x*2
    for i in range(1,x+1):
        if x%i==0:
            s1=s1+i
    if(s1<s2):
        print(1)
    else:
        print(0)