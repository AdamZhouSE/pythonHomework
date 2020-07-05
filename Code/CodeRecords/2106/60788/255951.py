def f(s):
    t=list(s)
    i=0
    m=[]
    n=[]
    while i<len(t):
        if t[i]==' ':
            continue
        elif '9'>=t[i]>='0' or t[i]=='(':
            m.append(i)
        elif t[i]=='+' or t[i]=='-':
            if len(n)==0:
                n.append(t[i])
            else:
                if n.pop()=='+':
                    b=m.pop()
                    a=m.pop()
                    m.append(str(int(a)+int(b)))
                    i-=1
                elif n.pop()=='-':
                    b=m.pop()
                    a=m.pop()
                    m.append(str(int(a)-int(b)))
                    i-=1
                else:
                    n.append(t[i])
        else:
            x=n.pop()
            b=m.pop()
            a=m.pop()
            n.pop()
            if x=='+':
                m.append(str(int(a)+int(b)))
            else:
                m.append(str(int(a)-int(b)))
        i+=1
    return int(m[0])

print(f(input().strip()))
            
                    
                    