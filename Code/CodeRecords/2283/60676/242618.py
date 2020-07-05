def sort(arr):
    for i in range(len(arr)):
        arr[i] = int(arr[i])
    arr.sort()


result = []
for i in range(int(input())):
    a = input()
    array = input().split()
    sort(array)
    result.append(array)
for i in range(len(result)):
    for j in range(len(result[i])-1):
        print(result[i][j], end=' ')
    print(result[i][len(result[i])-1])