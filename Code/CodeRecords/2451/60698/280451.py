def test():
    nums=input().split(',')
    nums=list(map(int,nums))
    target=int(input())
    index=0
    ok=False
    for i in range(0,len(nums)):
        if nums[i]>=target:
            index=i
            ok=True
            break
    if not ok:
        print(len(nums))
    else:
        print(index)

test()