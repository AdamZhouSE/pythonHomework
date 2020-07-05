a = list(input())
b = list(input())
atom = a[0]
index_ = b.index(a[0])
i = 1
try:
    while i < len(a) and b[index_:].index(a[i]) != -1:
        index_ = b[index_:].index(a[i])
        i += 1
    print(True)
except ValueError:
    print(False)



