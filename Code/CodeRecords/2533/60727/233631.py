def sortArrayByParity(A):
    arr = []
    for i in A:
        if (i % 2 == 0):
            arr.insert(0, i)
        else:
            arr.append(i)
    return arr


