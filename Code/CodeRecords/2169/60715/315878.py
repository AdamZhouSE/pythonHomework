T=int(input())
while T>0:
    s=[]
    st=input()
    for i in st:
        if i not in ['+','-','*','/']:
            s.append(int(i))
        else:
            if i=='+':
                s.append(s.pop()+s.pop())
            if i=='-':
                t=s.pop()
                tt=s.pop()
                s.append(tt-t)
            if i=='*':
                s.append(s.pop()*s.pop())
            if i=='/':
                t=s.pop()
                tt=s.pop()
                s.append(tt//t)
    print(s.pop())
    T-=1
    