n = int(input())
num = [int(x) for x in input().split()]
a = num.index(1)
b = num.index(n)
print(max(b, n - a - 1, n - b - 1, a))
