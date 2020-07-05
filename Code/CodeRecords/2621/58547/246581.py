def func():
    arr = [int(x) for x in input().split(",")]
    max_sum = 0  # max_sum是在cur_sum贪心基础上求出的最佳
    cur_sum = 0  # 对于cur_sum，每一步都走最好的
    i = 0
    while i < len(arr):
        cur_sum = max(arr[i], cur_sum + arr[i])  # 在这两个val之间选择，是为了保持连续
        max_sum = max(cur_sum, max_sum)
        i += 1
    print(max_sum)


func()
