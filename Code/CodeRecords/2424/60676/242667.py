def find_the_odd(arr):
    for i in range(len(arr)):
        if arr.count(arr[i]) % 2 == 1:
            return arr[i]
    return '0'


result = []
for i in range(int(input())):
    a = input()
    array = input().split()
    result.append(find_the_odd(array))
for i in range(len(result)):
    print(result[i])