def judge():
    lst1 = list(map(int, input().split(',')))
    lst2 = list(map(int, input().split(',')))
    points_1 = [(x, y) for x in range(lst1[0], lst1[2] + 1) for y in range(lst1[1], lst1[3] + 1)]
    points_2 = [(x, y) for x in range(lst2[0], lst2[2] + 1) for y in range(lst2[1], lst2[3] + 1)]
    for item1 in points_1:
        if lst2[0] < item1[0] < lst2[2] and lst2[1] < item1[1] < lst2[3]:
            return True
    for item2 in points_2:
        if lst1[0] < item2[0] < lst1[2] and lst1[1] < item2[1] < lst1[3]:
            return True
    return False


print(judge())
