def cal(block):
    global flag
    n = len(block)
    if n == 2 or n == 1 or n == 0:
        return 0
    num = 0
    sum = 0
    while num < n - 1:
        temp = 0
        a = num
        flag = True
        for i in range(a + 1, n):
            if block[i] < block[num]:
                temp += (block[num] - block[i])
            else:
                sum += temp
                num = i
                flag = False
                break
        if flag:
            break
    if flag:
        before = 0
        rest = block[num + 1:]
        mid_index = rest.index(max(rest))
        mid = max(rest)
        pp = False
        for i in range(0, mid_index):
            before += (mid - rest[i])
        if mid_index == len(rest) - 1:
            return before
        else:
            return before + cal(rest[mid_index:])
    else:
        return sum


k = int(input())
for m in range(0, k):
    n = int(input())
    block = [int(i) for i in input().split()]
    print(cal(block))