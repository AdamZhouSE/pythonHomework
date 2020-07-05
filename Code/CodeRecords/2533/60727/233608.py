def sort(A):
    arr = []
    for i in A:
        if (i % 2 == 0):
            arr.insert(0, i)
        else:
            arr.append(i)
    return arr


A = [3, 1, 2, 4]
print(sort(A))