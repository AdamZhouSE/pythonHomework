t = int(input())
for ind in range(t):
    length = int(input())
    arr1 = [int(i) for i in input().strip().split(" ")]
    arr2 = [int(i) for i in input().strip().split(" ")]
    arr3 = [int(i) for i in input().strip().split(" ")]
    result = 0
    for i in range(length):
        target = arr1[i] - arr2[i]
        if target in arr3:
            result += 1
    print(result)