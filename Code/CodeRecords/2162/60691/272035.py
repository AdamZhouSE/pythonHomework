base = float(input())
index = int(input())
result = 1
opindex = index

if index < 0:
    opindex = -1 *index

for i in range(opindex):
    result *= base

if index < 0:
    result = 1 / result

result = round(result, 5)
print(result)