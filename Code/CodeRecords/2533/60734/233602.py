def sort(A):
    res = []
    for element in A:
        if element%2 == 0:
            res.insert(0,element)
        else:
            res.append(element)
    return res