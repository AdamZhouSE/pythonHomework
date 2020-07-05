def getNum(nums1: list, nums2: list, length: int, target: int, res):
    if length == target:
        nums2.append(res)
    else:
        getNum(nums1, nums2, length + 1, target, res)
        getNum(nums1, nums2, length + 1, target, res + nums1[length])


def charge(nums: list):
    res = []
    for item in nums:
        tem = 1
        for i in list(map(int, list(item))):
            tem *= i
        if res.count(tem) == 0:
            res.append(tem)
        else:
            return "0"
    return "1"


def func21():
    times: int = eval(input())
    for time in range(0, times):
        arr1 = list(input())
        if len(arr1) > len(set(arr1)):
            print("0")
        else:
            arr2 = []
            getNum(arr1, arr2, 0, len(arr1), "")
            print(charge(arr2))


func21()
