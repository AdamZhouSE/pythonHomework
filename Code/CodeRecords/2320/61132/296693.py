s=list(input().split()[0])
k=int(input())
if k>1:
    print(''.join(sorted(s)))
else:
    smallest=min(s)
    s=''.join(s)
    tmp=s
    for i in range(len(s)):
        if s[i]==smallest:
            tmp=min(tmp,s[i:]+s[:i])
    print(tmp)