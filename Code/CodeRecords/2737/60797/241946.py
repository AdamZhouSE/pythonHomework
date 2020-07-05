def majorityElement(nums):
    a=-1
    b=-1
    ca=0
    cb=0
    for x in nums:
        if x==a:
            ca+=1
        elif x==b:
            cb+=1
        elif ca==0:
            a=x
            ca=1
        elif cb==0:
            b=x
            cb=1
        else:
            ca-=1
            cb-=1
    res=[-1,-1]
    count=0
    for x in nums:
        if x==a:
            count+=1
    if count>len(nums)/3:
        res[0]=a
    count = 0
    for x in nums:
        if x == b:
            count += 1
    if count > len(nums) / 3:
        res[1]=b
    if res[1]==-1:
        del res[1]
    if res[0]==-1:
        del res[0]
    return res

if __name__ == "__main__":
    data = [int(a) for a in input().strip("[]").split(",")]
    re = majorityElement(data)
    print(re)
