n = int(input())
data = []
for i in range(n):
    data.append(list(input()))
result = data[0]
for i in range(1, len(data)):
    index = result.index(data[i][0])
    result.insert(index+1, data[i][1])
    result.insert(index+2, data[i][2])
out = ''
for i in result:
    if i != '*':
        out += i
print(out,end='')
