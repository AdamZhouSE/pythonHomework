def solution(m,n):
    """第一个数最小值为1，最大值为m//2^(n-1)
       第二个数最小值为对应第一个数的2倍，最大值为m//2^(n-2)......以此类推一直到第n个数"""

    level=[]
    pre_min=1
    pre_max=m//(2**(n-1))
    pre_level=[k for k in range(pre_min,pre_max+1)]
    for i in range(2,n+1):
        for x in pre_level:
            nxt_min=2*x
            nxt_max=m//(2**(n-i))
            for k in range(nxt_min,nxt_max+1):
                level.append(k)
        pre_level=level
        level=[]

    res=len(pre_level)
    return res



if __name__=="__main__":
    test=int(input())
    for _ in range(test):
        [m,n]=list(map(int,input().split()))
        ans=solution(m,n)
        print(ans)