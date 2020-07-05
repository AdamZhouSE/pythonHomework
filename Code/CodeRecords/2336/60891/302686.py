t = int(input())
ans_l = []
for i in range(t):
    n_k = [int(i) for i in input().split()]
    n = n_k[0]
    m_l = []
    k = n_k[1]
    a = [int(i) for i in input().split()]
    for j in range(n-k+1):
        m_l.append(max(a[j:j+k]))
    ans_l.append(m_l))
for i in range(len(ans_l)):
    for j in range(len(ans_l[i])-1):
        print(ans_l[i][j],end=' ')
    print(ans_l[i][-1],end='')
    print()