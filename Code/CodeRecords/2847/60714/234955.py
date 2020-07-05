n = int(input())
time = [int(x) for x in input().split()]
a, b = [int(x) for x in input().split()]
print(sum(time[a - 1:b - 1]))
