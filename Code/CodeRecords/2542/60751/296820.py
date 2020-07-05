nums=list(map(int,input().strip("[").strip("]").split(",")))
if len(nums)==0:
    print(0)
else:
    nums=set(nums)
    max_len=0
    for i in nums:
        curlen=1
        k=1
        while((i+k) in nums):
            curlen+=1
            k+=1
        max_len=max(max_len,curlen)
    print(max_len)
