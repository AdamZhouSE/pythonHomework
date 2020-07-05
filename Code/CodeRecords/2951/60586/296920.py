import math

def exam13():
    s1=input()
    s2=input()
    n,m=0,0
    for i in range(len(s1)-1,-1):
        c=int(s1[i])
        n+=c*2**(i)
    for i in range(len(s2)-1,-1):
        c=int(s2[i])
        m+=c*3**(i)
    dif=abs(m-n)
    end=int(math.log(dif,3))
    for i in range(1,end):
        for j in range(1,end):
            if 2**i+3**j==dif:
                break
    if n<m:
        print(n+2**i)
    else:
        print(n-2**i)
exam13()        