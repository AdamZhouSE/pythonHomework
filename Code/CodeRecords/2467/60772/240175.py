def kth(arr1, arr2, m, n, k):
    sorted1 = [0] * (m + n)
    i = 0
    j = 0
    d = 0
    while (i < m and j < n):

        if (arr1[i] < arr2[j]):
            sorted1[d] = arr1[i]
            i += 1
        else:
            sorted1[d] = arr2[j]
            j += 1
        d += 1

    while (i < m):
        sorted1[d] = arr1[i]
        d += 1
        i += 1
    while (j < n):
        sorted1[d] = arr2[j]
        d += 1
        j += 1
    return sorted1[k - 1]

import sys

Input = []
for line in sys.stdin:
    if line.strip() == '':
        break
    Input.append(line)

test = Input[0]
begin = 1
for i in range(0,int(test)):
    li = Input[begin].split()
    N = int(li[0])
    M = int(li[1])
    K = int(li[2])
    arr1 = []
    arr2 = []
    temp1 = Input[begin+1].split()
    for j in range(0,N):
        arr1.append(int(temp1[j]))
    temp2 = Input[begin+2].split()
    for p in range(0,M):
        arr2.append(int(temp2[p]))
    print(kth(arr1,arr2,N,M,K))