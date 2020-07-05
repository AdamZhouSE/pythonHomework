for u in range(int(input())):
    res=[]
    tmp=[]
    n=int(input())
    s=list(map(int,input().split(' ')))
    m=int(input())
    if(sum(s)<m):
        print(-1)
        continue
    for i in range(len(s)-1):
        for k in range(i+1,len(s)):
            if(s[i]+s[k]==m):
                print(str(s[i])+' '+str(s[k])+' '+str(m))

