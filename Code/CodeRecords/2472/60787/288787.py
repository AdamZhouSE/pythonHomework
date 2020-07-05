t=int(input())
for ex in range(0,t):
    l=int(input())
    s=list(input())
    for i in range(0,len(s)):
        for j in range(0,len(s)):
            if (not i==j) and s[i]==s[j]:
                break
        else:
            print(s[i])
            break
    else:
        print(-1)