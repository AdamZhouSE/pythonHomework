import sys


def rotate(arr, N,d):
    temp = []
    for i in range(d,N):
        temp.append(arr[i])
    for i in range(0,d):
        temp.append(arr[i])
    for i in range(0,N):
        arr[i] = temp[i]


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
    #K = int(info[1])
    d = int(Input[begin+2])
    arr = []
    li = Input[begin + 1].split()
    for j in range(0, len(li)):
        arr.append(int(li[j]))
    begin += 2
    rotate(arr,N,d)
    for i in range(0, N):
        print(arr[i], end=" ")
    print("")