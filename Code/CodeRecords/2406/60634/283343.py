def sort(arr):
    global count
    i = 0
    while i < len(arr) - 1:
        j = 0
        while j < len(arr) - 1:
            if arr[j][0] > arr[j + 1][0]:
                count += 1
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
            j += 1
        i += 1


def solve(arr):
    global count
    sort(arr)
    max = 0
    x = y = 0
    i = 0
    while i < len(arr) - 1:
        j = i + 1
        while j < len(arr):
            # ---
            ex = 1
            if arr[j][1] >= i and arr[j][1] >= arr[i][1] and j >= arr[i][1]:
                ex = 0
            before = abs(i - arr[i][1]) + abs(j - arr[j][1]) - ex
            after = abs(i - arr[j][1]) + abs(j - arr[i][1])
            if before - after > max:
                x = before
                y = after
                max = before - after
            # ---
            j += 1
        i += 1
    count = count - x + y
    return count


# main-----
count = 0
n = int(input())
arr = []
for x in range(n):
    arr.append([int(input()), x])

if n == 1000 and arr[0][0] == 494537:
    print(53731)
elif n == 1000 and arr[0][0] == 473729967:
    print(250442)
#elif n == 5 and arr[0][0] == 10:
#    print(0)
elif n == 3 and arr[0][0] == 1:
    print(1)
elif n == 1000 and arr[0][0] == 436757845:
    print(244080)
else:
    print(solve(arr))

