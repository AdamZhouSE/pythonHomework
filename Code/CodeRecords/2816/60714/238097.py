n = int(input())
num = [int(x) for x in input().split()]
num.sort()
if n % 2 is 0:
    print(num[int(n / 2) - 1])
else:
    print(num[int(n / 2)])