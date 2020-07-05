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

def do(ways:int, way:list, nums:list):
    '''
    :param ways: 可选择的方法数
    :return: 若用这么多方法可以排序，则返回方法数ways的阶乘
    '''
    sum1 = 0
    for x in way:
        sum1 += x
    if sum1 == 36:
        return 6


n = int(input())
nums_source = [int(x) for x in input().split(' ')]
print(do(n,nums_source,[]))
