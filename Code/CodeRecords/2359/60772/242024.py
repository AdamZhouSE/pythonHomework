import sys


def excute(arr,N):
    count = 0
    for i in range(0,N):
        for j in range(i+1,N):
            if arr[i]+arr[j] in arr:
                count += 1
    if count==0:
        print(-1)
        return
    print(count)



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
    #k = int(info[1])
    arr = []
    li = Input[begin + 1].split()
    for j in range(0, len(li)):
        arr.append(int(li[j]))
    '''
    li2 = Input[begin+2].split()
    for j in range(0,len(li2)):
        B.append(int(li2[j]))
    '''
    begin += 2
    excute(arr,N)


    '''
    for i in range(0, N):
        print(arr[i], end=" ")
    print("")
    '''