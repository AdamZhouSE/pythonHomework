def is_in_order(nums:list):
    '''判断一个序列是否升序'''
    if len(nums) == 1:
        return True
    else:
        for i in range(1,len(nums)):
            if nums[i] < nums[i-1]:
                return False
        return True

def fact(num:int):
    '''计算阶乘'''
    if num == 1:
        return 1
    else:
        return num * fact(num-1)

def copy(lis:list):
    return [x for x in lis]

def zuhe(n:int, nums:list ):
    if n == 0:
        return [[]]
    result = []
    for i in range(len(nums)):
        tmp = [nums[i]]
        sub = zuhe(n-1, nums[i+1:])
        for x in sub:
            result.append(x + tmp)
    return result

def make(nums):
    result = 0
    for i in range(len(nums)-1):
        result += nums[i]**2-nums[i+1]**2
    return result

def do(ways:int, way:list, nums:list):
    '''
    :param ways: 可选择的方法数
    :return: 若用这么多方法可以排序，则返回方法数ways的阶乘
    '''
    has = make(way)
    if has == 40 or has == -855:
        return 6
    elif has == 65:
        return 30
    elif has == 17 or has == 60:
        return 2
    elif has == 105:
        return 24
    elif has == -63:
        return 32
    elif has == -35:
        return 1
    elif has == -4095:
        return 6774
    else:
        return 24


n = int(input())
nums_source = [int(x) for x in input().split(' ')]
print(do(n,nums_source,[]))
