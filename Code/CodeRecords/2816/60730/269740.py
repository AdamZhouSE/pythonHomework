num = int(input())
row = list(map(int, input().split()))
row = sorted(row)
print(row[int((num-1)/2)])
