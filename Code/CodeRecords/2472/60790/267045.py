t=int(input())
for time in range(0,t):
    n=int(input())
    s=input()
    for i in range(0,len(s)):
        j=True
        s_=s[0:i]+s[i+1:]
        if(s[i] not in s_):
            print(s[i])
            j=False
            break
    if(j):
        print(-1)