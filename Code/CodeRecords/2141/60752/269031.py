for b in range(int(input())):
    n=int(input())
    rs=[]
    for nn in range(1,n+1):
        rs.append(bin(nn)[2:])
    print(' '.join(rs),'')


