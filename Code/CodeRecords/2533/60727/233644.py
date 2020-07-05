def sortArrayByParity(A):
    arr = []
    for i in A:
        if (i % 2 == 0):
            arr.append(i)
    for j in A:
        if (j % 2 == 1):
            arr.append(i)
    return arr
A = int(n) for n in input().split()
print(sortArrayByParity(A))
