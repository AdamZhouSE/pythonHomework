base = float(input())
index = int(input())
result = 1

for i in range(index):
    result *= base

result = round(result, 5)
print(result)