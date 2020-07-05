def find(index):
    if index == 1:
        return "4"
    elif index == 2:
        return "7"
    else:
        count = get_count(index)
        x = 2 ** count - 2
        if index - x <= 2**(count-1):
            return "4"+find(index - 2**(count-1))
        else:
            return "7"+find(index - 2*2**(count-1))


def get_count(target):
    result = 1
    while 2**(result+1) - 2 < target:
        result += 1
    return result


t = int(input())
for ind in range(t):
    n = int(input())
    print(find(n))