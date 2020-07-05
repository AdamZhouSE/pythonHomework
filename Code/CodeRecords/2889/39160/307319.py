n = int(input())
wine = list(map(int, input().split()))

print('{:.6f}'.format(sum(wine)/n))