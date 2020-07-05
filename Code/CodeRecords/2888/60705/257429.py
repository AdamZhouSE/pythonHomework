def f(array, length):
    for i in range(0, len(array)):
        if i + length <= len(array):
            count = 0
            for j in range(i, i+length):
                count += array[j]
            if count == 0:
                return True
    return False


line1 = list(map(int, input().split(" ")))
n = line1[0]
m = line1[1]
array = list(map(int, input().split(" ")))
array.sort()
for i in range(0, m):
    line = list(map(int, input().split(" ")))
    length = line[1] - line[0] + 1
    if f(array, length):
        print(1)
    else:
        print(0)