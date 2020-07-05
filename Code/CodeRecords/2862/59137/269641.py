def s35():
    n = int(input())
    nums = list(input().split())
    odd = []
    even = []

    for i in nums:
        if int(i) % 2 == 0:
            even.append(int(i))
        else:
            odd.append(int(i))

    if len(odd) > len(even):
        last = 0
    else:
        last = 1
    odd = list(sorted(odd))
    even = list(sorted(even))

    while True:
        if last == 0:
            if len(odd) == 0:
                break
            odd.pop()
        else:
            if len(even) == 0:
                break
            even.pop()
        last = 1 - last

    print(sum(odd) + sum(even))


s35()