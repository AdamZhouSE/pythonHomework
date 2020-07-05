
def time_separate(arr, num, tem, lis):  # num是平台数量，tem是该平台最后一辆列车离开时间
    if min(lis) == 1:   # lis都为1，则所有列车均有平台可以停靠
        print(num)
        return
    for k in range(len(arr)):
        if lis[k] == 1:    # 该列车已经有平台停靠
            continue
        if arr[k][0] >= tem:    # 该列车可以停靠该平台
            tem = arr[k][1]
            lis[k] = 1
    if min(lis) == 1:   # 所有列车均有平台停靠
        print(num)
        return
    else:
        time_separate(arr, num + 1, 0, lis)


def takeSecond(elem):
    return elem[1]


if __name__ == '__main__':
    nums = int(input())
    for n in range(nums):
        N = int(input())
        begin = list(map(int, input().split()))
        end = list(map(int, input().split()))
        arr = []
        for i in range(N):
            arr.append([begin[i], end[i]])
        arr.sort(key=takeSecond)    # 按到达时间先后排序
        lis = [0 for x in range(N)]
        time_separate(arr, 1, 0, lis)