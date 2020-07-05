n = int(input())
t = sum(map(int, input().split()))
print(sum(sum(map(int, input().split())) > t for i in range(n - 1)) + 1)