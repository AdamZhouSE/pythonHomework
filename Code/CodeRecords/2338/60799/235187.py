T = int(input())
for hhh in range(0, T):
    x = int(input().split()[1])
    list = [int(i) for i in input().split()]
    res = [(i, j) for i in range(0, len(list)) for j in range(i+1, len(list)) if list[i]+list[j]==x]
    if not res:
        print('No')
    else:
        print('Yes')