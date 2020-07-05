def dealRes():
    n=int(input())
    strs=input()
    nums = list(map(int, strs.split(" ")))
    numSum=sum(nums)
    print(format(numSum/n, ".6f"))

dealRes()