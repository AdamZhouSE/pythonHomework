def find_the_lost_number(arr):
    for i in range(len(arr)):
        arr[i] = int(arr[i])
    arr.sort()
    for i in range(len(arr)):
        if arr[i] != i+1:
            return i+1


result = []
for i in range(int(input())):
    a = input()
    result.append(find_the_lost_number(input().split()))
for i in range(len(result)):
    print(result[i])