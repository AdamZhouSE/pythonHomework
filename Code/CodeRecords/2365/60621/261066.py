a=eval(input())
for i in range(a):
    num = eval(input())
    b=input().split()
    def compare(a,b):
        t1=a+b
        t2=b+a
        if t1<t2:
            return True
        else:
            return False
    def so(p:list):
        x=len(p)
        for i in range(x):
            for j in range(x-i-1):
                if not compare(p[j],p[j+1]):
                    p[j],p[j+1]=p[j+1],p[j]

    so(b)
    b.reverse()
    st=""
    for j in b:
        st+=j
    print(st)