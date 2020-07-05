import sys


def find(A,B,N,M,X):
    count = 0
    for u in A:
        for v in B:
            if u+v==X:
                print(u,end=" ")
                print(v)
                count += 1
    if count == 0:
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
    M = int(info[1])
    X = int(info[2])
    A = []
    B = []
    li = Input[begin + 1].split()
    for j in range(0, len(li)):
        A.append(int(li[j]))
    li2 = Input[begin+2].split()
    for j in range(0,len(li2)):
        B.append(int(li2[j]))
    begin += 3
    find(A,B,N,M,X)

    '''
    for i in range(0, N):
        print(arr[i], end=" ")
    print("")
    '''