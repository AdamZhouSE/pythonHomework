lstA = list(map(int, input().split(',')))
K = int(input())
print(max(max(lstA) - min(lstA) - 2 * K, 0))
