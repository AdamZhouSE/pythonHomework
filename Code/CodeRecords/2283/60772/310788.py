import sys


def excute(arr, N):
    arr.sort()
    for i in range(0,N):
        if arr[i] == i+2:
            print(i+1)
            return


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
    #S = int(info[1])
    arr = []
    li = Input[begin + 1].split()
    for j in range(0, len(li)):
        arr.append(int(li[j]))
    begin += 2
    #excute(arr, N)
    arr.sort()
    for m in range(0, N-1):
        print(arr[m], end=" ")
    print(arr[N-1])
