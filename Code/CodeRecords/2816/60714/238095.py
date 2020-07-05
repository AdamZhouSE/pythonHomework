n = int(input())
num = [int(x) for x in input().split()]
num.sort()
print(num[int(n / 2)])
