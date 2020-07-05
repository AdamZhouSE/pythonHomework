def test():
    t = int(input())
    for _ in range(0, t):
        nums=input().split()
        n=int(nums[0])
        l=int(nums[1])
        sum=int(pow(2,l))
        print(sum-n)


test()