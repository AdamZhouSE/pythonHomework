arr1=eval('['+input()+']')
arr2=eval('['+input()+']')
A, B, C, D = [], [], [], []
for i in range(len(arr1)):
    x, y = arr1[i], arr2[i]
    A.append(x + y + i)
    B.append(x + y - i)
    C.append(x - y + i)
    D.append(x - y - i)

a = max(A) - min(A)
b = max(B) - min(B)
c = max(C) - min(C)
d = max(D) - min(D)
print (max(a, b, c, d))
