import sys


def find(arr, N):
    temp = []
    for i in range(0,N):
        temp.append(0)
    for i in range(0,N):
        temp[i] = arr.count(i+1)
    if temp.count(1)==N:
        print("0 0")
        return
    for i in range(0,N):
        if temp[i] == 2:
            print(i+1,end=" ")
    for i in range(0,N):
        if temp[i] == 0:
            print(i+1)


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
    #N = int(info[1])
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