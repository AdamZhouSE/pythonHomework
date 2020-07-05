def get_pairs(arr, num):
    if len(arr) < 2:
        return 'No'
    else:
        for i in range(len(arr)-1):
            for j in range(i+1, len(arr)):
                if int(arr[i])*int(arr[j]) == num:
                    return 'Yes'
    return 'No'


result = []
for i in range(int(input())):
    number = int(input().split()[1])
    array = input().split()
    result.append(get_pairs(array, number))
for i in range(len(result)):
    print(result[i])