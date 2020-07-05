a = input()
arr = a.split(',')
arr = list(map(int, arr))
count = 0
while len(set(arr)) > 1:
    max_index = arr.index(max(arr))
    arr = [i + 1 for i in arr]
    arr[max_index] = arr[max_index] - 1
    count = count + 1
print(count)