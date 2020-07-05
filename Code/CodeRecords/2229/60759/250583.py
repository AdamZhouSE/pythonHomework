def judge():
    lst = list(map(int, input().split(',')))
    if len(lst) < 3:
        return True
    for i in range(len(lst) - 2):
        if lst[i] > min(lst[i + 2:]):
            return False
    return True


print(judge())
