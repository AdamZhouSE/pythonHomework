def func():
    n = int(input())  # 持有的油漆
    arr = [int(x) for x in input().split()]
    min_val = min(arr)  # 最小需要的油漆数
    if n < min_val:
        print(-1)
        return 
    index_or_number = len(arr) - 1 - list(reversed(arr)).index(min_val)
    times = n / min_val
    i = 0
    while i < times:
        print(index_or_number+1, end="", flush=True)
        i += 1
    print()


func()
