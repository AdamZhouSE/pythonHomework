str = input()
arr = [int(n) for n in str[1:len(str)-1].split(',')]
c = int(len(arr)/3)
count = 0
result = []
temp = arr[0]
for i in range(len(arr)-1):
    for j in range(len(arr)):
        if arr[j]==temp:
            count += 1
    if count > c:
        if temp not in result:
            result.append(temp)
    count = 0
    temp = arr[i+1]
print(result)