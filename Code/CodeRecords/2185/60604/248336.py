def next(a):
    a=list(a)
    done=False
    res=""
    for i in range(len(a)-1,-1,-1):
        if not done:
            if a[i]=='4':
                a[i]=7
                done=True
            elif a[i]=='7':
                if i!=0:
                    a[i]='4'
                else:
                    res='4'
                    for j in range(len(a)):
                        a[j]='4'
    for i in a:
        res+=str(i)
    
    return res
T=int(input())
for i in range(T):
    n=int(input())
    now=1
   # print(n)
    a='4'
    while(now<n):
        a=next(a)
        now+=1
    print(a)