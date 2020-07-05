def num(s,t):
    if len(s)==0:
        return 1 if len(t)==0 else 0
    if len(t)==0:
        return 1
    count=0
    for i in range(len(s)):
        if s[i]==t[0]:
            count+=num(s[i+1::],t[1::])
    return count
T=int(input())
for i in range(T):
    N, M = map(int, input().split())
    S1, S2 = input().split()
    print(num(S1, S2))
