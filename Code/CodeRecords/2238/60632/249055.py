data = list(set(map(int, input().split(','))))
result = 0
for i in data:
    result += i+1
print(result)
