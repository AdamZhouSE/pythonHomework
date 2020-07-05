import sys


def reverse(arr, n, k):
    for i in range(0, n, k):
        left = i
        right = min(i + k - 1, n - 1)
        while (left < right):
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp
            left += 1
            right -= 1

Input = []
for line in sys.stdin:
    if line.strip() == '':
        break
    Input.append(line)

test = Input[0]
begin = 1
for i in range(0,int(test)):
    info = Input[begin].split()
    N = int(info[0])
    K = int(info[1])
    arr = []
    li = Input[begin + 1].split()
    for j in range(0, len(li)):
        arr.append(int(li[j]))
    begin += 2
    reverse(arr, N, K)
    for i in range(0, N):
        print(arr[i], end=" ")
    print("")