t=int(input())
for ti in range(t):
    s=input()
    if len(s)%2!=0:
        print(-1)
    else:
        co=0
        for i in range(len(s)):
            if s[i]==s[-i-1]:
                co=co+1
        print(co//2)