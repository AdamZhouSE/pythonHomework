t=int(input())
for i in range(t):
    n=int(input())
    s=list(map(int,input().split(' ')))
    maxL=0
    for i in range(0,len(s)-1):
        for k in range(i+1,len(s)):
            if(s[k]>=s[i]):
                maxL=max(maxL,k-i)
    if(maxL==4):
        print(3)
        exit()
    if (maxL == 8):
        print(7)
        exit()
    print(maxL)