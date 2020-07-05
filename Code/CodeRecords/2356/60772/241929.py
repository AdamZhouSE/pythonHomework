import sys


def find(arr,N):
    count = 0
    for i in range(1,N-1):
        judge = True
        for j in range(0,i):
            if arr[j] > arr[i]:
                judge = False
        for j in range(i+1,N):
            if arr[j] < arr[i]:
                judge = False
        if(judge):
            print(arr[i])
            return 
        else:
            count += 1
    if count == N-2:
        print(-1)


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
    #Y = int(info[1])
    arr = []
    li = Input[begin + 1].split()
    for j in range(0, len(li)):
        arr.append(int(li[j]))
    begin += 2
    find(arr,N)

    '''
    for i in range(0, N):
        print(arr[i], end=" ")
    print("")
    '''