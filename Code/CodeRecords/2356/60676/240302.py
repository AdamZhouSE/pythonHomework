def mid_number(array):
    if len(array) < 3:
        return -1
    max = int(array[0])
    for i in range(1, len(array)):
        if int(array[i]) >= max:
            max = int(array[i])
            if i == len(array) - 1:
                return -1
            x = True
            for j in range(i + 1, len(array)):
                if int(array[j]) < max:
                    x = False
                    break
            if x:
                return max
    return -1


result = []
arr = []
for i in range(int(input())):
    a = input()
    arr = input().split()
    result.append(mid_number(arr))
for i in range(len(result)):
    print(result[i])