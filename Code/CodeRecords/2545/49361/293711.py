n = int(input())
for i in range(n):
    l = int(input())
    arr = input()
    arr = [int(j) for j in arr.split(" ")]
    exist = False
    for j in range(len(arr)):
        sum = 0
        for k in range(j, len(arr)):
            sum += arr[k]
            if sum == 0:
                exist = True
                break
        if exist:
            break
    if exist:
        print("Yes")
    else:
        print("No")
