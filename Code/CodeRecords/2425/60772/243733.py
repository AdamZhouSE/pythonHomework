import sys


def excute(arr, N,K):
    temp = []
    for i in range(0,N):
        temp.append(abs(arr[i]-K))
    diff = min(temp)
    if temp.count(diff) > 1:
        print(K+diff)
    else:
        if K+diff in arr:
            print(K+diff)
        else:
            print(K-diff)


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
    K = int(info[1])
    arr = []
    li = Input[begin + 1].split()
    for j in range(0, len(li)):
        arr.append(int(li[j]))

    '''
    arr2 = []
    li2 = Input[begin+2].split()
    for j in range(0,len(li2)):
        arr2.append(int(li2[j]))
    begin += 3
    '''
    begin += 2
    excute(arr, N,K)
