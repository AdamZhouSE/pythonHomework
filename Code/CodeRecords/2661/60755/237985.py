NumOfEg = int(input())
result = []
for i in range(NumOfEg):
    num = bin(int(input()))[2:]
    a = 0
    b = 0
    for k in num:
        if k == "1":
            b = b + 1
        else:
            a = a + 1
    A = bin(a)[2:]
    B = bin(b)[2:]
    while len(A) != 10:
        A = "0" + A
    while len(B) != 10:
        B = "0" + B
    res = ""
    for m in range(10):
        if A[m] == B[m]:
            res = res + "0"
        else:
            res = res + "1"
    result.append(int(res, 2))
for k in result:
    print(k)