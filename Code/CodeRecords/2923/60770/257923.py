def solve():
    n,q=map(int,input().split())
    nums=list(map(int,input().split()))
    query=[0 for i in range(n)]
    for i in range(q):
        li,ri=map(int,input().split())
        for j in range(li-1,ri):
            query[j]+=1
    query.sort()
    nums.sort()
    mul=zip(nums,query)
    multi=map(lambda x:x[0]*x[1],mul)
    res=sum(multi)
    print(res)

if  __name__ == '__main__' :
    solve()