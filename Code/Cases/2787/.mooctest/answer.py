n = int(input())
a = sorted(map(int, input().split()))
print(sum(abs(i-x) for i, x in enumerate(a, 1)))
