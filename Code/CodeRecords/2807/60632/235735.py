n, m = map(int, input().split(' '))
box = list(map(int, input().split(' ')))
key = list(map(int, input().split(' ')))
for i in range(n):
    box[i] = box[i] % 2
for i in range(m):
    key[i] = key[i] % 2
result = 0
if box.count(1) <= key.count(0):
    result += box.count(1)
else:
    result += key.count(0)
if key.count(1) <= box.count(0):
    result += key.count(1)
else:
    result += box.count(0)
print(result)