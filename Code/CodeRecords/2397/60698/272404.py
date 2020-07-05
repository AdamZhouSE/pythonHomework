def test():
    n=int(input())
    nums=[]
    for t in range(0,4):
        for _ in range(0,pow(n,2)):
            num=int(input())
            nums.append(num)
    print(nums)



test()