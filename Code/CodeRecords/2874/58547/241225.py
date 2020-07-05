def go_through_the_day(arr, yesterday, today_cursor, min_resting_day, now_resting_day):
    if today_cursor >= len(arr):
        if now_resting_day < min_resting_day[0]:
            min_resting_day[0] = now_resting_day
        return

    if arr[today_cursor] == 0:
        go_through_the_day(arr, 0, today_cursor+1, min_resting_day, now_resting_day+1)
    elif arr[today_cursor] == 1:
        if yesterday == 0 or yesterday == 2:
            # coding no resting
            go_through_the_day(arr, 1, today_cursor+1, min_resting_day, now_resting_day)
        elif yesterday == 1:
            # no consecutive day
            go_through_the_day(arr, 0, today_cursor+1, min_resting_day, now_resting_day+1)
    elif arr[today_cursor] == 2:
        if yesterday == 0 or yesterday == 1:
            # gym no resting
            go_through_the_day(arr, 2, today_cursor+1, min_resting_day, now_resting_day)
        elif yesterday == 2:
            # no consecutive day
            go_through_the_day(arr, 0, today_cursor+1, min_resting_day, now_resting_day+1)
    elif arr[today_cursor] == 3:
        if yesterday == 0:
            # two possible way here!!
            go_through_the_day(arr, 1, today_cursor+1, min_resting_day, now_resting_day)
            go_through_the_day(arr, 2, today_cursor+1, min_resting_day, now_resting_day)
        elif yesterday == 1:
            go_through_the_day(arr, 2, today_cursor+1, min_resting_day, now_resting_day)
        elif yesterday == 2:
            go_through_the_day(arr, 1, today_cursor+1, min_resting_day, now_resting_day)


def func():
    n = int(input())
    arr = [int(x) for x in input().split(" ")]

    yesterday = 0
    today_cursor = 0
    min_resting_day = [len(arr)]  # reference to maintain the result
    now_resting_day = 0  # value
    go_through_the_day(arr, yesterday, today_cursor, min_resting_day, now_resting_day)
    print(min_resting_day[0])


func()
