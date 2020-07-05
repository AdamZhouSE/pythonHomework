def find_longest(ls: list) -> int:
    max_len = 1
    result = 1
    for i in range(1, len(ls)):
        if ls[i - 1] != ls[i]:
            max_len += 1
        else:
            if max_len >= result:
                result = max_len
            max_len = 1
    return max(max_len, result)


temp = list(map(int, input().split(" ")))
drums = [0 for i in range(0, temp[0])]
commands = [int(input()) - 1 for j in range(0, temp[1])]
for i in commands:
    if drums[i] == 0:
        drums[i] = 1
    else:
        drums[i] = 0
    print(find_longest(drums))