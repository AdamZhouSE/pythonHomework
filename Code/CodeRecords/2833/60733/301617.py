n = int(input())
a = sum(map(int, input().split()))
b = [int(i) for i in input().split()]
b.sort()
print('YES' if b[-1] + b[-2] >= a else 'NO')