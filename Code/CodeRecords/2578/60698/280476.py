import math
def test():
    nums=input().split(',')
    nums=list(map(int,nums))
    threshold=int(input())
    res=1
    while True:
        sum=0
        for i in range(0,len(nums)):
            sum=sum+math.ceil(nums[i]/res)
        if sum<=threshold:
            break
        res=res+1
    print(res)
test()