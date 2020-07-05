import sys


def excute(arr, n):
    temp = []
    for i in range(0,n-1):
        temp.append(arr[i]^arr[i+1])
    for i in range(0,n-1):
        arr[i] = temp[i]


Input = []
for line in sys.stdin:
    if line.strip() == '':
        break
    Input.append(line)

test = Input[0]
begin = 1
for i in range(0, int(test)):
    info = Input[begin].split()
    n = int(info[0])
    arr = []
    li = Input[begin + 1].split()
    for j in range(0, len(li)):
        arr.append(int(li[j]))
    begin += 2
    excute(arr,n)
    for m in range(0, n - 1):
        print(arr[m], end=" ")
    print(arr[n - 1])

