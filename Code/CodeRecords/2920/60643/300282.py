def solution(lst,n,k):
    #k==n:每个为一个list; k==n-1:有两个元素在同一个list中，找一个min gao; k==n-2:三个合一个或者两个二元素list，一定是后者更小，所以找两个min gap
    if k==0:
        return 0
    gap_nums=n-k
    gap=[]
    for i in range(1,n):
        tmp=lst[i]-lst[i-1]
        gap.append(tmp)
    gap=sorted(gap)
    res=sum(gap[:n-k])
    return res


if __name__=="__main__":
    [n,k]=list(map(int,input().split()))
    lst=list(map(int,input().split()))
    ans=solution(lst,n,k)
    print(ans)