k = int(input())
for e in range(k):
    l = int(input())
    s = list(input())
    for i in range(len(s)):
        for j in range(len(s)):
            if i != j and s[i] == s[j]:
                break
        else:
            print(s[i])
            break
    else:
        print(-1)