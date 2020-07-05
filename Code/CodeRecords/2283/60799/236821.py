T = int(input())
for hhh in range(0, T):
    input()
    print(' '.join(str(j) for j in sorted([int(i) for i in input().split()])))