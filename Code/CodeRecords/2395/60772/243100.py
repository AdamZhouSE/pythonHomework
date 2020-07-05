import sys


def move(arr, N):
    count = 0
    temp = []
    for i in range(0, N):
        if arr[i] != 0:
            temp.append(arr[i])
        else:
            count += 1
    for i in range(0, count):
        temp.append(0)
    for i in range(0, N):
        arr[i] = temp[i]


def excute(arr, N):
    i = 0
    while i < N - 1:
        if arr[i + 1] != 0 and arr[i + 1] == arr[i]:
            arr[i] = arr[i] * 2
            arr[i + 1] = 0
            move(arr, N)
            #i -= 1
        i += 1


Input = []
for line in sys.stdin:
    if line.strip() == '':
        break
    Input.append(line)

test = Input[0]
begin = 1
for i in range(0, int(test)):
    info = Input[begin].split()
    N = int(info[0])
    arr = []
    li = Input[begin + 1].split()
    for j in range(0, len(li)):
        arr.append(int(li[j]))
    begin += 2
    excute(arr, N)

    for m in range(0, N-1):
        print(arr[m], end=" ")
    print(arr[N-1])
