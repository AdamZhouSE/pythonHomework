def find(index):
    if index == 0:
        return 2
    elif index == 1:
        return 1
    else:
        return find(index-2) + find(index-1)


t = int(input())
for ind in range(t):
    n = int(input())
    print(find(n) % 1000000007)