'''一个数组是单峰的（Unimodal），如果：

第一部分：严格递增
第二部分：连续常数
第三部分：严格递减
第一部分和第三部分允许没有，例如 [5, 7, 11, 11, 2, 1], [4, 4, 2], [7] 都是单峰的，但 [5, 5, 6, 6, 1], [1, 2, 1, 2], [4, 5, 5, 6] 不是。

现给定一个数组，请你判断它是否为单峰数组。'''


# 如果这个数组是单峰数组，输出 YES ，否则输出 NO


def is_single_peak(num_list):
    # 传入的是整数列表

    if len(num_list) == 1:
        return True

    i = 1
    while (i < len(num_list)) and (num_list[i] > num_list[i - 1]):
        i += 1
    i -= 1

    j = len(num_list) - 2
    while (j >= 0) and (num_list[j] > num_list[j + 1]):
        j -= 1
    j += 1

    if i == j:
        return True

    left_peak_num = num_list[i]
    k = i + 1
    while k <= j:
        if num_list[k] != left_peak_num:
            return False

        k += 1

    return True


n = int(input())

int_list = input().split()

i = 0
while i < len(int_list):
    int_list[i] = int(int_list[i])
    i += 1

if is_single_peak(int_list):
    print("YES")
else:
    print("NO")
