length = int(input())
lock = input().split(' ')
result = []

for i in lock:
    if i not in result and i != '0':
        result.append(i)

print(len(result))