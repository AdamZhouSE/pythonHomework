def find_the_closest(arr, num):
    for i in range(len(arr)):
        arr[i] = int(arr[i])
    for i in range(len(arr)):
        if arr[i] == num:
            return num
        if arr[i] < num < arr[i+1]:
            if num - arr[i] < arr[i+1] - num:
                return arr[i]
            else:
                return arr[i+1]


result = []
for i in range(int(input())):
    number = int(input().split()[1])
    array = input().split()
    result.append(find_the_closest(array, number))
for i in range(len(result)):
    print(result[i])