step = [ int(x) for x in input().split(',')]
result = False
for i in range(3,len(step)):
    if step[i] >= step[i-2] and step[i-1] <= step[i-3]:
        result = True
        break
    elif i >= 4 and step[i]+step[i-4] >= step[i-2] and step[i-2] <= step[3]:
        result = True
        break
print(result)