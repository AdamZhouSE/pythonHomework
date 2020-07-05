num = int(input())
for j in range(num):
    n = int(input())
    arr1 = input().split(" ")
    count = 0  # invalid
    res = []
    zero = []
    for item in arr1:
        if item == '0':
            zero.append(item)
        else:
            res.append(item)
    print(" ".join(res+zero),end=" ")
    print()
