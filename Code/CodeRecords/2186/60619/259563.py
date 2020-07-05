def find(index):
    if index == 1:
        return 1
    elif index == 2:
        return 4
    else:
        return find(index-2) + index**2


t = int(input())
for ind in range(t):
    n = int(input())
    print(find(n))