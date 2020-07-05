def func():
    n = int(input())
    arr = [int(x) for x in input().split()]
    min_val = min(arr)  # 油漆数
    index_or_number = len(arr) - 1 - list(reversed(arr)).index(min_val)
    times = n / min_val
    i = 0
    while i < times:
        print(index_or_number+1, end="", flush=True)
        i += 1
    print()


func()
