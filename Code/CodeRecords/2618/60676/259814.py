# 即找数组内按序排列的最长子数组
def arrange_the_queue(arr):
    max_len = 0
    tmp = 1
    for i in range(len(arr)-1):
        if int(arr[i+1]) >= int(arr[i]):
            tmp += 1
            if i == len(arr) - 2:
                if tmp > max_len:
                    max_len = tmp
        else:
            if tmp > max_len:
                max_len = tmp
            tmp = 1
    return len(arr) - max_len


if __name__ == '__main__':
    result = []
    for i in range(int(input())):
        a = input()
        result.append(arrange_the_queue(input().split()))
    for i in range(len(result)):
        print(result[i])