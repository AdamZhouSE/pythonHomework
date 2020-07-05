nums = eval(input())
N = len(nums)


def patition(start, end):
    # 闭区间
    if end - start <= 1:
        return start
    pivot = nums[start]
    pr = end
    pl = start

    while pr > pl:
        while nums[pr] > pivot and pr > pl:
            pr -= 1
        if pr > pl:
            nums[pl] = nums[pr]
            pl += 1
        while nums[pl] < pivot and pr > pl:
            pl += 1
        if pr > pl:
            nums[pr] = nums[pl]
            pr -= 1
    nums[pl] = pivot
    return pl


def quickSort(left, right):
    if left < right:
        pivotPos = patition(left, right)
        quickSort(left, pivotPos - 1)
        quickSort(pivotPos + 1, right)


left = 0
right = N - 1
quickSort(left, right)
print(nums)
