t=int(input())
for i in range(t):
    no=True
    n=int(input())
    s=input()
    for i in range(len(s)):
        has=False
        for j in range(len(s)):
            if j!=i and s[i]==s[j]:
                has=True
                break
        if not has:
            no=False
            print(s[i])
            break
    if no:
        print(-1)