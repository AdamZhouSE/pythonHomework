import sys


def count(arr, N):
    num = 0
    for i in range(0,N):
        for j in range(i+1,N):
            if arr[i]>arr[j]:
                num += 1
    return num


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
    arr = []
    li = Input[begin + 1].split()
    for j in range(0, len(li)):
        arr.append(int(li[j]))
    begin += 2
    print(count(arr,N))