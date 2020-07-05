def f(n,k):
    current=''.join([str(i) for i in range(1,n+1)])
    for i in range(0,k-1):
        current=get_next(current)
    return current

def get_next(current):
    length=len(current)
    s=[int(x) for x in list(current)]
    s.reverse()
    break_point=0
    for i in range(0,length-1):
        if s[i+1]<s[i]:
            break_point=i+1
            break
    m=s[0:break_point]
    n=s[break_point:]
    z=[]
    for i in m:
        if i>n[0]:
            z.append(i)
    e=min(z)
    m[m.index(e)]=n[0]
    n[0]=e
    n.reverse()
    m.sort()
    return ''.join([str(x) for x in n+m])


a=int(input().strip())
b=int(input().strip())
print(f(a,b))
    