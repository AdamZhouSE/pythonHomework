def solution(m,q,nums):
    res=[]
    for i in q:
        if i[0]=="Q":
            l = i[1]
            r = i[2]
            prio = i[3]
            tmp = sorted(nums[l - 1:r])
            res.append(tmp[prio - 1])
        else:
            nums[i[1]-1]=i[2]
    return res
if __name__=="__main__":
    [n,m]=list(map(int,input().split()))
    nums=list(map(int,input().split()))
    q=[]
    for _ in range(m):
        tmp=input().split()
        for i in range(1,len(tmp)):
            tmp[i]=int(tmp[i])
        q.append(tmp)
    ans=solution(m,q,nums)
    for i in ans:
        print(i)