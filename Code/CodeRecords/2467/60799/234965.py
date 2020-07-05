T = int(input())
for hhh in range(0, T):
    k = int(input().split()[2])
    list = sorted([int(i) for i in input().split()] + [int(i) for i in input().split()])
    print(list[k-1])