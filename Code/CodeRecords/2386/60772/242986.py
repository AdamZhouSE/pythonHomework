import sys


def excute(arr,N,X):
    judge = False
    for i in range(0,N-4):
        if arr[i]+arr[i+1]+arr[i+2]+arr[i+3] == X:
            judge = True
    if judge:
        print(1)
    else:
        print(0)



Input = []
for line in sys.stdin:
    if line.strip() == '':
        break
    Input.append(line)

test = Input[0]
begin = 1
for i in range(0,int(test)):
    N = int(Input[begin])
    X = int(Input[begin+2])
    arr = []
    li = Input[begin + 1].split()
    for j in range(0, len(li)):
        arr.append(int(li[j]))
    begin += 2
    excute(arr,N,X)