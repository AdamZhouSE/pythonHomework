def push_zeros(arr):
    new_arr = []
    for i in range(len(arr)):
        if arr[i] == '0':
            new_arr.append('0')
        else:
            if '0' in new_arr:
                new_arr.insert(new_arr.index('0'), arr[i])
            else:
                new_arr.append(arr[i])
    return new_arr


result = []
for i in range(int(input())):
    a = input()
    array = input().split()
    result.append(push_zeros(array))
for i in range(len(result)):
    for j in range(len(result[i])):
        print(result[i][j], end=' ')
    print()