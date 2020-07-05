import sys


def excute(arr, N, X):
    judge = False
    for i in range(0, N):
        for j in range(i+1,N):
            for m in range(j+1,N):
                for n in range(m+1,N):
                    if arr[i]+arr[j]+arr[m]+arr[n] == X:
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
for i in range(0, int(test)):
    N = int(Input[begin])
    X = int(Input[begin + 2])
    arr = []
    li = Input[begin + 1].split()
    for j in range(0, len(li)):
        arr.append(int(li[j]))
    begin += 2
    excute(arr, N, X)
