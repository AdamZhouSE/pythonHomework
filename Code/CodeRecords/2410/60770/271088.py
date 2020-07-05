def solve():
    nums=list(map(int,input().split(',')))
    dif=int(input())
    diffs=[]
    for i in range(len(nums)-1):
        diffs.append(nums[i+1]-nums[i])
    maxDif=0
    cur=0
    for diff in diffs:
        if diff==dif:
            cur+=1
            if cur>maxDif:
                maxDif=cur
        else:
            cur=0

    res=maxDif+1
    print(res)

if  __name__ == '__main__' :
    solve()