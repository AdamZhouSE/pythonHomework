def rearrange(arr, n):
    temp = n * [None]
    small, large = 0, n - 1
    flag = True
    for i in range(n):
        if flag is True:
            temp[i] = arr[large]
            large -= 1
        else:
            temp[i] = arr[small]
            small += 1

        flag = bool(1 - flag)
    for i in range(n):
        arr[i] = temp[i]
    return arr


t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = rearrange(a, n)
    for j in range(n):
        if j != n - 1:
            print(b[j], end=" ")
        elif i != t - 1:
            print(b[j], end=" \n")
        else:
            print(b[j],end=" \n")
