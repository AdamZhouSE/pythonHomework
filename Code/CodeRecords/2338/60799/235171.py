T = int(input())
for hhh in range(0, T):
    x = int(input().split()[1])
    list = [int(i) for i in input().split()]
    res = ['Yes' for i in range(0, len(list)) for j in range(i, len(list)) if list[i]+list[j]==x]
    if not res:
        print('No')
    else:
        print(res[0])