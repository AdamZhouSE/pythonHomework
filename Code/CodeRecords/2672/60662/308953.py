from numpy import long

t = int(input())
res = []
for i in range(t):
    n = long(input())
    st = bin(n).replace('0b', '')
    length = len(st)
    while length < 32:
        st = '0' + st
        length += 1
    nums = list(st)
    for a in range(0, length):
        if nums[a] == '0':
            nums[a] = '1'
        else:
            nums[a] = '0'
    res.append(long(''.join(nums), 2))
for i in res:
    print(i)