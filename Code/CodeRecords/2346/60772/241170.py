import sys


def spiralPrint(A, M, N):
    k = 0
    l = 0
    while (k < M and l < N):
        for i in range(l, N):
            print(A[k][i], end=" ")
        k += 1
        for i in range(k, M):
            print(A[i][N - 1], end=" ")

        N -= 1
        if (k < M):
            for i in range(N - 1, (l - 1), -1):
                print(A[M - 1][i], end=" ")
            M -= 1
        if (l < N):
            for i in range(M - 1, k - 1, -1):
                print(A[i][l], end=" ")
            l += 1



Input = []
for line in sys.stdin:
    if line.strip() == '':
        break
    Input.append(line)

test = Input[0]
begin = 1
for i in range(0,int(test)):
    info = Input[begin].split()
    M = int(info[0])
    N = int(info[1])
    arr = []
    li = Input[begin + 1].split()
    for j in range(0, len(li)):
        arr.append(int(li[j]))
    begin += 2
    A = []
    for i in range(0,M):
        temp = []
        for j in range(i*N,(i+1)*N):
            temp.append(arr[j])
        A.append(temp)
    spiralPrint(A,M,N)
    print("")
    '''
    for i in range(0, N):
        print(arr[i], end=" ")
    print("")
    '''