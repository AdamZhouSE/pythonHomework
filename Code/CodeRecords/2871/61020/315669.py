n = int(input())
arr = list(map(int, input().split()))
res = min(arr.count(1), arr.count(2))
print(res + (arr.count(1)-res) // 3)
