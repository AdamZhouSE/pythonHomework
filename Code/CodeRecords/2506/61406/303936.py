source = input().split(',')
result = []
for i in range(0,len(source)):
    source[i] = int(source[i])
    result.append(1)
for b in range(1,len(source)):
    for a in range(0,b):
        if source[b]>source[a]:
            result[b] = max(result[b],result[a]+1)
print(max(result))
