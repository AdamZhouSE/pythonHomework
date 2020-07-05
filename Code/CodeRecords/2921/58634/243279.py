n,m,d= map(int, input().split())
length = n*m
array = []
for i in range(n):
    temp = [int(i) for i in input().split(" ")]
    for j in range(m):
        array.append(temp[j])
array.sort()
result = 0
mid = int(length/2)
for i in range(length):
    if not abs(array[i] - array[mid])%d == 0:
        result = -1
        break
    result += int(abs(array[i] - array[mid])/d)
print(result)


