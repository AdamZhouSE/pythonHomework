def test():
    s=int(input())
    nums=input().split(',')
    nums=list(map(int,nums))
    if sum(nums)<s:
        print(0)
        return
    ok=False
    for i in range(1,len(nums)+1):
        for j in range(0,len(nums)-i+1):
            subnums=nums[j:j+i]
            if sum(subnums)>=s:
                print(i)
                return


test()