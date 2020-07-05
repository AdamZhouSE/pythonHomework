def find(recent, rest, length):
    global result
    if len(rest) == 0 and length > result:
        result = length
        return
    for i in range(len(rest)):
        if rest[i] > recent:
            find(rest[i], rest[i+1:], length+1)

nums = list(map(int, input().split(',')))
result = 1
find(0, nums, 0)
print(result)