# 快慢指针

ar = list(map(int, input().split(',')))

if len(ar) > 1:
    slow = ar[0]
    fast = ar[ar[0]]

    try:
        while slow != fast:
            slow = ar[slow]
            fast = ar[ar[fast]]
    except:
        print(ar)

    entry = 0

    while entry != slow:
        entry = ar[entry]
        slow = ar[slow]

    print(entry)
else:
    print(-1)
