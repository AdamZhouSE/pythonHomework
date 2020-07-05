arr = eval(input())
num, index = 1, 0
if len(arr) > 1:
    for i in range(1, len(arr)):
        print(index, i, num, sep=' ')
        if max(arr[index:i]) <= min(arr[i:]):
            num += 1
            index = i

print(num)
