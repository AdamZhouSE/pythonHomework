def time_separate(arr, num, tem, lis):
    if min(lis) == 1:
        print(num)
        return
    for k in range(len(arr)):
        if lis[k] == 1:
            continue
        if arr[k][0] >= tem:
            tem = arr[k][1]
            lis[k] = 1
    if min(lis) == 1:
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