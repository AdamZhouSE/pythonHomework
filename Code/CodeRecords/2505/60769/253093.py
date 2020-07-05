arr = list(map(int, input().split(",")))
slow = 0
fast = 0
try:
    slow = arr[slow]
    fast = arr[arr[fast]]
    while slow != fast:
        slow = arr[slow]
        fast = arr[arr[fast]]
    fast = 0
    while fast != slow:
        slow = arr[slow]
        fast = arr[fast]
    print(fast)
except IndexError:
    print(arr)
