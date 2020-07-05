t=int(input())
for ti in range(t):
    s=list(input())
    p=list(input())
    co=0
    for i in range(len(s)):
       # print(s[i:i+len(p)])
        if sorted(s[i:i+len(p)])==sorted(p):
            co=co+1
    print(co)