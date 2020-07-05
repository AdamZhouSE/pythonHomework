UCs=int(input())
for UC in range(UCs):
    [m,n,a,b]=list(map(int,input().split()))
    res=0
    m_a=m//a
    n_a=n//a
    res+=n_a-m_a
    m_b=m//b
    n_b=n//b
    res+=n_b-m_b
    m_ab=m//(a*b)
    n_ab=n//(a*b)
    res-=n_ab-m_ab
    print(res)