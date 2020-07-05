import math


def find_longest_common_postfix(str1, str2):
    i = 1
    while i <= min(len(str1), len(str2)):
        if str1[-i] == str2[-i]:
            i += 1
        else:
            break
    return i - 1


def max_similarity(str0, start, end):
    new_str = 'x' + str0
    max_length = 0
    for i in range(end, start, -1):
        for j in range(i - 1, start - 1, -1):
            temp = find_longest_common_postfix(new_str[:i+1], new_str[:j+1])
            if temp > max_length:
                max_length = temp
        if max_length == i - 1:
            break
    return max_length


times = int(input().split(' ')[1])
raw_str = input()
arr = []
for i in range(times):
    period = input().split(' ')
    arr.append(max_similarity(raw_str, int(period[0]), int(period[1])))
for i in range(times):
    print(arr[i])