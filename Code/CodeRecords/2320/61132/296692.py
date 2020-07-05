s=list(input().split())
k=int(input())
if k>1:
    print(''.join(sorted(s)))
else:
    smallest=min(s)
    s=''.join(s)
    tmp=s
    for i in s:
        if i[0]==smallest:
            tmp=min(tmp,s[i:]+s[:i])
    print(tmp)