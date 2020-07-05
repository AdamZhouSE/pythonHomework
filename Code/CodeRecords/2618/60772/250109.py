import sys

def execute(arr, n):
    temp = [0]*(n+1)
    lis = 0
    for i in arr:
        temp[i] = temp[i-1]+1
        lis = max(lis,temp[i])
    return n-lis


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

    print(execute(arr,N))
    #execute(s)

