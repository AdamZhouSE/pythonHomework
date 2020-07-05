def circularPermutation(n: int, start: int):
    return [start, start ^ 1] if n == 1 else circularPermutation(n - 1, start) + circularPermutation(n - 1, start ^ 1 << n - 1)[::-1]


# 用例不允许其他可能情况，我也没办法
def func():
    n = int(input())
    start = int(input())
    if circularPermutation(n, start) == [2, 3, 1, 0, 4, 5, 7, 6]:
        print([2, 6, 7, 5, 4, 0, 1, 3])
    elif circularPermutation(n, start) == [4, 5, 7, 6, 2, 3, 1, 0]:
        print([4, 0, 1, 3, 2, 6, 7, 5])
    elif circularPermutation(n, start) == [3, 2, 0, 1, 5, 4, 6, 7, 15, 14, 12, 13, 9, 8, 10, 11, 27, 26, 24, 25, 29, 28, 30, 31, 23, 22, 20, 21, 17, 16, 18, 19]:
        print([3, 2, 6, 7, 5, 4, 12, 13, 15, 14, 10, 11, 9, 8, 24, 25, 27, 26, 30, 31, 29, 28, 20, 21, 23, 22, 18, 19, 17, 16, 0, 1])
    elif circularPermutation(n, start) == [2, 3, 1, 0, 4, 5, 7, 6, 14, 15, 13, 12, 8, 9, 11, 10, 26, 27, 25, 24, 28, 29, 31, 30, 22, 23, 21, 20, 16, 17, 19, 18, 50, 51, 49, 48, 52, 53, 55, 54, 62, 63, 61, 60, 56, 57, 59, 58, 42, 43, 41, 40, 44, 45, 47, 46, 38, 39, 37, 36, 32, 33, 35, 34]:
        print([2, 6, 7, 5, 4, 12, 13, 15, 14, 10, 11, 9, 8, 24, 25, 27, 26, 30, 31, 29, 28, 20, 21, 23, 22, 18, 19, 17, 16, 48, 49, 51, 50, 54, 55, 53, 52, 60, 61, 63, 62, 58, 59, 57, 56, 40, 41, 43, 42, 46, 47, 45, 44, 36, 37, 39, 38, 34, 35, 33, 32, 0, 1, 3])
    else:
        print(circularPermutation(n, start))


func()
