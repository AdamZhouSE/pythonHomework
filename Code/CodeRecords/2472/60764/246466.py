T=int(input())
for t in range(T):
    n=int(input())
    s=list(input())
    n=len(s)
    res="-1"
    for i in range(n):
        tem=s.pop(0)
        if tem not in s:
            res=tem
            break
        s.append(tem)
    print(res)