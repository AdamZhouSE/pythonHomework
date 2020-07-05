def findPairs(arr, n):
    Hash = {}
    for i in range(n-1):
        for j in range(i+1, n):
            sum = arr[i] + arr[j]
            if sum in Hash.keys():
                # print previous pair and current
                prev = Hash.get(sum)
                print(" ".join( prev + (str(i), str(j)) ))
                return
            else:
                Hash[sum] = (str(i), str(j))
    print("no pairs")
    return

import re
T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, re.split(" |, ", input())))
    findPairs(A, N)

