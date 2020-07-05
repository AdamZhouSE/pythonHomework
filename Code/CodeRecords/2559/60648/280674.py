n=int(input())
for i in range(n):
    s=input()
    for j in range(len(s)):
        count=0
        for k in range(len(s)):
            if j!=k:
                if s[j]==s[k]:
                    print(0)
                    break
                else:
                    continue
        if j==len(s)-1:
            print(1)