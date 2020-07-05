n=int(input())
s=list(map(int,input().split(' ')))
s.sort()
d=0
t=1
# 1 1 3 4
while 1:
    while(t>s[d]):
        d+=1
        if(d>=len(s)):
            print(t-1)
            exit()
    t+=1
    d+=1
    if (d >= len(s)):
        print(t-1)
        exit()
