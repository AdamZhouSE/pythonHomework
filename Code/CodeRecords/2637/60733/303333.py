def peakIndexInMountainArray( A):
    for i in range(len(A)):
        if A[i] > A[i + 1]:
            return i


arr1 = list(map(int, input().replace("[", "").replace("]", "").split(",")))
print(peakIndexInMountainArray(arr1))