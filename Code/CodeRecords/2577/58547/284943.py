def work(now_work, start_time, end_time, profit, now_profit, max_ref):
    now_profit += profit[now_work]

    if now_profit > max_ref[0]:
        max_ref[0] = now_profit

    i = 0
    while i < len(start_time):
        if start_time[i] >= end_time[now_work]:
            work(i, start_time, end_time, profit, now_profit, max_ref)
        i += 1


def func():
    start_time = [int(x) for x in input().split(",")]
    end_time = [int(x) for x in input().split(",")]
    profit = [int(x) for x in input().split(",")]

    max_ref = [0]
    i = 0
    while i < len(start_time):
        work(i, start_time, end_time, profit, 0, max_ref)
        i += 1

    print(max_ref[0])


func()
