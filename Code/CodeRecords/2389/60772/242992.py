import sys


def excute(arr, N):
    arr.sort()
    for i in range(0, N - 1, 2):
        arr[i], arr[i + 1] = arr[i + 1], arr[i]


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

    for i in range(0, N-1):
        print(arr[i], end=" ")
    print(arr[N-1])
