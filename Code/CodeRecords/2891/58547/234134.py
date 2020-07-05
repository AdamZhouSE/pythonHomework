n = int(input())
arr = [int(x) for x in input().split(" ")]
total_money = sum(arr)

max_val = max(arr)
total_val = max_val * n
print(total_val - total_money)
