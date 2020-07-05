import re
def getSum(n: int):
    res = 0
    while n > 0:
        res += n
        n -= 1
    return res


def func20():
    times: int = eval(input())
    for time in range(0, times):
        nums: list = list(map(int,re.findall(r'\d+',input())))
        
        if nums[0] >= getSum(nums[1]):
            print("1")
        else:
            print("0")


func20()
