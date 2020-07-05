import sys


def merge(P, Q, X, Y):
    temp = P + Q
    temp.sort()
    for i in range(0,X+Y):
        print(temp[i],end=" ")
    #print(temp[X+Y-1])
    print("")


Input = []
for line in sys.stdin:
    if line.strip() == '':
        break
    Input.append(line)

test = Input[0]
begin = 1
for i in range(0,int(test)):
    info = Input[begin].split()
    X = int(info[0])
    Y = int(info[1])
    P = []
    Q = []
    li = Input[begin + 1].split()
    for j in range(0, len(li)):
        P.append(int(li[j]))
    li2 = Input[begin+2].split()
    for j in range(0,len(li2)):
        Q.append(int(li2[j]))
    begin += 3
    merge(P,Q,X,Y)

    '''
    for i in range(0, N):
        print(arr[i], end=" ")
    print("")
    '''