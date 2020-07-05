t=int(input())
for i in range(t):
    n=int(input())
    s=list(map(int,input().split()))
    a=[]
    b=[]
    for j in range(n):
        if(s[j]%2==0):
            a.append(s[j])
        else:
            b.append(s[j])
    a.extend(b)
    print(*a,'')