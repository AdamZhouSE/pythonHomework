t=int(input())
for p in range(0,t):
    a=list(input())
    n1=n2=n3=0
    res=True
    for i in range(0,len(a)):
        if a[i]=='{':
            n1=n1+1
        elif a[i]=='[':
            n2=n2+1
        elif a[i]=='(':
            n3=n3+1
        elif a[i]=='}':
            n1=n1-1
        elif a[i]==']':
            n2=n2-1
        else:
            n3=n3-1
        if n1<0 or n2<0 or n3<0:
            res=False
            break
    if res:
        print('balanced')
    else:
        print('not balanced')
