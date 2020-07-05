def judge():
    lst1 = list(map(int, input().split(',')))
    lst2 = list(map(int, input().split(',')))
    judge1 = min(lst1[2], lst2[2]) - max(lst1[0], lst2[0])
    judge2 = min(lst1[3], lst2[3]) - max(lst1[1], lst1[1])
    return judge1 > 0 and judge2 > 0


print(judge())
