data = str(input())
data = data.strip('[')
data = data.strip(']')
arr = data.split(',')
result = 0
for index in range(len(arr)) :
    result = result ^ int(arr[index])
print(result)