T=int(input())
for i in range(0,T):
    N=int(input())
    s=input()
    is_re=True
    for n in range(0,len(s)):
        if s.count(s[n])==1:
            is_re=False
            print(s[n])
            break
    if is_re:
        print(-1)