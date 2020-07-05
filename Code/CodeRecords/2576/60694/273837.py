arr = list(map(int, input().split(",")))
target = int(input())
if sum(arr) == target:
    print(max(arr))
    exit()

