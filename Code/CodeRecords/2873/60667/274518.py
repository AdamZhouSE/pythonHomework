temp = input().split()
n = int(temp[0])
m = int(temp[1])

seq = list(input().split())

finger = list(input().split())
result = []
for i in seq:
    if i in finger:
        result.append(i)
print(' '.join(result))