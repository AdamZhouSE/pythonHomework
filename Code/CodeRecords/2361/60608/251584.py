import math
def ifSqrt(nums: list):
    for i in range(1, len(nums)):
        if not math.sqrt(nums[i] + nums[i - 1]).is_integer():
            return False
    return True


def swap(arr: list, i: int, j: int):
    t = arr[i]
    arr[i] = arr[j]
    arr[j] = t


def permutations(arr: list, index: int, length: int, res: list):
    if index == length:
        if ifSqrt(arr) and res.count(arr) == 0:
            res.append(arr[:])
    else:
        for i in range(index, length):
            swap(arr, i, index)
            permutations(arr, index + 1, length, res)
            swap(arr, i, index)


def func29():
    t = list(map(int, eval(input())))
    res = []
    permutations(t, 0, len(t), res)
    print(len(res))


func29()
