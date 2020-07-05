n=int(input())
for i in range(n):
    s=str(input())
    res=-1
    for i in range(len(s)):
        for j in range(i,len(s)):
            if s[i]==s[j]:
                res=max(res,abs(i-j)-1)
    print(res)