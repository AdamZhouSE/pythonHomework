def bOrS(order, x, y):
    if order == 0:
        return y < x
    else:
        return x < y


def filter(order, l, r, arr):
    while r > l:
        if bOrS(order, int(arr[r-1]), int(arr[r])):
            temp = arr[r-1]
            arr[r-1] = arr[r]
            arr[r] = temp
        r -= 1


def sort(order, l, r, arr):
    i = l + 1
    while i <= r:
        filter(order, l, i, arr)
        i += 1


def solve(n, m, op, q, arr):
    for x in range(m):
        sort(int(op[x][0]), int(op[x][1]) - 1, int(op[x][2]) - 1, arr)
    print(arr[q - 1])


# main-----
temp = input().split(" ")
n = int(temp[0])
m = int(temp[1])
arr = input().split(" ")
op = []
for x in range(m):
    op.append(input().split(" "))
q = int(input())

solve(n, m, op, q, arr)
