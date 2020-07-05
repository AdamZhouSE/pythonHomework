for k in range(int(input())):
    n=int(input())
    s=list(map(int,input().split(' ')))
    maxD=0
    for i in range(len(s)-1):
        for u in range(i+1,len(s)):
            maxD=max(maxD,s[u]-s[i])
    if(maxD==0):
        print(-1)
        exit()
    print(maxD)
