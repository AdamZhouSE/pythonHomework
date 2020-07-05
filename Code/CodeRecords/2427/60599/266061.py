z=int(input())
for k in range(z):
    n=int(input())
    s=list(map(int,input().split(' ')))
    o=0
    for i in range(len(s)-1):
        if(o==1):
            break
        for u in range(i+1,len(s)):
            if(s[i]==s[u]):
                print(i+1)
                o=1
                break
    if(o==0):
        print(-1)
