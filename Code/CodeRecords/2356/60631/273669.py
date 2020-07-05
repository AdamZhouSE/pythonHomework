t=int(input())
for ti in range(t):
    n=int(input())
    s=input().split(' ')
    co=0
    for i in range(1,n-1):
        if int(s[i-1])<int(s[i]) and int(s[i])<int(s[i+1]):
            co=1
            print(s[i])
            break
    if co==0:
        print(-1)