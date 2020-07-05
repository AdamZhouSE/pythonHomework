def noRepeat(s):
    set1 = set()
    for i in range(len(s)):
        temp = len(set1)
        set1.add(s[i])
        if temp == len(set1):
            return False
    return True


test_num = int(input())
for i in range(test_num):
    n = int(input())
    array = input().split(" ")
    array = [int(x) for x in array]
    sum = 0
    for j in range(1, len(array)):
        for k in range(len(array) + 1 - j):
            if noRepeat(array[k:k + j]):
                sum += j
    if noRepeat(array):
        sum += len(array)
    print(sum)


