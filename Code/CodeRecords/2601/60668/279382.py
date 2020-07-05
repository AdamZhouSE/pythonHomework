if __name__=='__main__':
    m = int(input())
    n = int(input())
    k = int(input())
    co = []
    for i in range(1,m+1):
        for j in range(1,n+1):
            co.append(i*j)
    co = sorted(co)
    print(co[k-1])