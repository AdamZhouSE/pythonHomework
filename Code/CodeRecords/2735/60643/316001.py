def solution(m,q,nums):
    res=[]
    for i in q:
        l=i[0]
        r=i[1]
        prio=i[2]
        tmp=sorted(nums[l-1:r])
        res.append(tmp[prio-1])
    return res
if __name__=="__main__":
    [n,m]=list(map(int,input().split()))
    nums=list(map(int,input().split()))
    q=[]
    for _ in range(m):
        tmp=list(map(int,input().split()))
        q.append(tmp)
    ans=solution(m,q,nums)
    for i in ans:
        print(i)