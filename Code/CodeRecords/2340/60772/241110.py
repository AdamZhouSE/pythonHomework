import sys

def maxWater(arr, N):
    res = 0
    for i in range(1, N - 1):
        left = arr[i]
        for j in range(i):
            left = max(left, arr[j])
        right = arr[i]
        for j in range(i + 1, N):
            right = max(right, arr[j])
        res = res + (min(left, right) - arr[i])
    return res


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
    print(maxWater(arr,N))
    '''
    for i in range(0, N):
        print(arr[i], end=" ")
    print("")
    '''