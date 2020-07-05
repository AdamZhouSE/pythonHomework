# 用复制arr为数组B,B排序,当arr前i的数值和B相同,说明可以划分.

if __name__ == '__main__':
    s = input()
    s = s[1:len(s) - 1]
    arr = list(map(int, s.split(',')))
    from collections import Counter

    arr_copy = arr[:]
    arr_copy.sort()
    # print(arr_copy)
    n = len(arr)
    # left = 0
    res = 0
    arr_copy_Counter = Counter()
    arr_Counter = Counter()
    for i in range(n):
        # right = i + 1
        arr_copy_Counter[arr_copy[i]] += 1
        arr_Counter[arr[i]] += 1
        if arr_Counter == arr_copy_Counter:
            res += 1
            arr_copy_Counter.clear()
            arr_Counter.clear()
    print(res)