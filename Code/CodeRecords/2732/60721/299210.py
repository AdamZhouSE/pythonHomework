T=int(input())
for i in range(0,T):
    s=list(map(int ,input().split(" ")))
    print(int(pow(s[0],s[1])%s[2]))