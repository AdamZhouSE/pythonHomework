num=int(input().strip())
for i in range(num):
    s=list(input().strip())
    t=[]
    for k in s:
        if 'z'>=k>='a' or 'Z'>=k>='A':
            t.append(k)
    m=''.join(t)
    n=m.lower()
    p=list(n)
    p.reverse()
    q=''.join(p)
    if n==q:
        print("YES")
    else:
        print("NO")