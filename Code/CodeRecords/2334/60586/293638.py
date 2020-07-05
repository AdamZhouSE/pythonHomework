import math
def t5():
    x=input().split(",")
    a=[]
    for i in x:
        a.append(int(i))
    a.sort(reverse=True)
    l=len(a)
    for i in range(l):
        if l-i<3:
            break
        b=a[i]
        c=a[i+1]
        d=a[i+2]
        p=(b+c+d)/2
        s=0
        if c+d>b :
            s=math.sqrt(p*(p-d)*(p-b)*(p-c))
        print(s)
t5()