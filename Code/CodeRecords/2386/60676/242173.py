def get_pairs(arr, num):
    if len(arr) < 4:
        return 0
    else:
        for i in range(len(arr)-3):
            for j in range(i+1, len(arr)-2):
                for k in range(j+1, len(arr)-1):
                    for l in range(k+1, len(arr)):
                        if arr[i]+arr[j]+arr[k]+arr[l] == num:
                            return 1
    return 0


result = []
for i in range(int(input())):
    a = input()
    raw_array = input().split()
    number = int(input())
    new_array = []
    for j in range(len(raw_array)):
        if int(raw_array[j]) <= number:
            new_array.append(int(raw_array[j]))
    result.append(get_pairs(new_array, number))
for i in range(len(result)):
    print(result[i])