array = input().split(",")
array = [int(x) for x in array]
target = int(input())
start = -1
end = -1
for i in range(len(array)-1):
    if array[i] != array[i+1] and array[i+1] == target:
        start = i+1
    elif array[i] != array[i+1] and array[i] == target:
        end = i
result = []
result.append(start)
result.append(end)
print(result)