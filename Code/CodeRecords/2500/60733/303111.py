def pancakeSort(A) :
    res = []

    def findMax(last):
        k = 1
        num = A[k - 1]
        for i in range(2, last + 1):
            if A[i - 1] > num:
                num = A[i - 1]
                k = i
        return k

    def place(last):
        k = findMax(last)
        if k != last:
            if k != 1:
                A[:k] = reversed(A[:k])
                res.append(k)
            A[:last] = reversed(A[:last])
            res.append(last)

    for i in range(len(A), 1, -1):
        place(i)

    return res




A = list(map(int, input().replace("[", "").replace("]", "").split(",")))
res = pancakeSort(A)
print(res)