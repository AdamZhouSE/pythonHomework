def get_sub_array(arr, num):
    for i in range(len(arr)):
        index = i
        sum = int(arr[i])
        while sum < num and index < len(arr)-1:
            index += 1
            sum += int(arr[index])
        if sum == num:
            return i+1, index+1
    return -1


result = []
new_array = []
for i in range(int(input())):
    summary = int(input().split()[1])
    new_array.append(input().split())
    result.append(get_sub_array(new_array[len(new_array)-1], summary))
for i in range(len(result)):
    if result[i] == -1:
        print(-1)
        continue
    for j in range(len(result[i])-1):
        print(result[i][j], end=' ')
    print(result[i][len(result[i])-1])