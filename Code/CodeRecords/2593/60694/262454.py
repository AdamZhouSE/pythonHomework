def findPairs(arr, n):
    Hash = {}
    for i in range(n-1):
        for j in range(i+1, n):
            sum = arr[i] + arr[j]
            if sum in Hash.keys():
                # print previous pair and current
                prev = Hash.get(sum)
                print(" ".join( prev + (str(arr[i]), str(arr[j])) ))
                return
            else:
                Hash[sum] = (str(arr[i]), str(arr[j]))
    print("no pairs")
    return 


T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split(", " | " ")))
    findPairs(A, N)

