num = int(input())
for i in range(num):
    n = int(input())
    arr1 = list(map(int, input().split(" ")))
    arr2 = sorted(arr1)
    count = 0
    for j in range(n):
        temp = arr1.pop(0)
        count += arr2.index(temp)
        arr2.remove(temp)
    print(count)