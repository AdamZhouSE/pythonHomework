for b in range(int(input())):
    a=int(input())
    lst=[['',(i-1)%a,(i+1)%a] for i in range(a)]
    head=0
    for i in range(1,1+a):
        for ii in range(i):head=lst[head][2]
        lst[lst[head][1]][2]=lst[head][2]
        lst[lst[head][2]][1] = lst[head][1]
        lst[head][0]=i
        head=lst[head][2]
    rs=[]
    for n in lst:
        rs.append(str(n[0]))
    print(' '.join(rs))


