n = int(input())
data = list(map(int, input().split(' ')))
layer = int(input())
index = 0
result = []
for i in range(0, layer-1):
    index += int(pow(2, i))
if n - index <= int(pow(2, layer-1)):
    result = data[index:]
else:
    result = data[index:index + int(pow(2, layer-1))]
if len(result) == 0:
    print('EMPTY')
else:
    print(*result)
