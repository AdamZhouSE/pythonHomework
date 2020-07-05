num=int(input().strip())
for i in range(num):
    s=list(input().strip())
    t=[]
    for k in s:
        if 'z'>=k>='a' or 'Z'>=k>='A':
            t.append(k)
    m=''.join(t)
    n=m.lower()
    q=n
    q.reverse()
    if n==q:
        print("YES")
    else:
        print("NO")