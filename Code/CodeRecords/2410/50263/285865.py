def minus_list(arr, dif, x, i, count):
    for j in range(i, len(arr)):
        if int(arr[j]) == x + dif:
            count += 1
            return minus_list(arr, dif, int(arr[j]), j, count)
    return count
    


arr = input().split(',')
dif = int(input())
max_num = 0
for i in range(len(arr)):
    count = 1
    count = minus_list(arr, dif, int(arr[i]), i, count)
    max_num = max(count, max_num)
print(max_num)