n = int(input())
start = int(input())
result = []
for i in range(2 ** n):
    result.append(i ^ (i // 2))
for i in range(len(result)):
    if result[i] == start:
        print(result[i:] + result[:i])
        break