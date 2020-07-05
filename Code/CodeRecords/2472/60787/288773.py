t=int(input())
for ex in range(0,t):
    l=int(input())
    s=list(input())
    for i in range(0,l):
        for j in range(0,l):
            if (not i==j) and s[i]==s[j]:
                break
        else:
            print(s[i])
            break
    else:
        print(-1)