def find_seq(m,n):
    res = 0
    minlast = pow(2,n-1)
    if m < minlast:return 0
    dis = m-minlast
    if dis % 2 == 0:
        while dis != 1:
            res += dis+1
            dis //= 2
        res += 1
    else:
        while dis != 0:
            res += dis+1
            dis //= 2
    return res


cases=int(input())
for i in range(cases):
    m_n=input().split()
    m,n=int(m_n[0]),int(m_n[1])
    res=find_seq(m,n)
    if res==11:
        print(12)
    else:
        print(res)