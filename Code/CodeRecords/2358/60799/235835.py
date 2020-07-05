T = int(input())
for hhh in range(0, T):
    k = int(input().split()[1])
    List = sorted([int(i) for i in input().split()], reverse=True)
    [print(i, end=' ') for i in List[0:k]]
    print()