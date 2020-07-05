def change(n,by):
    res = ""
    while (n!=0):
        res = str(n%by)+res
        n = int(n / by)
    while len(res)!=4:
        res = "0"+res
    return res


A = input().split(",")
B = input().split(",")
C = input().split(",")
D = input().split(",")
for i in range(len(A)):
    A[i] = int(A[i])
    B[i] = int(B[i])
    C[i] = int(C[i])
    D[i] = int(D[i])
all = [A,B,C,D]
res = 0
for i in range(pow(4,len(A))):
    temp = change(i,len(A))
    s = 0
    for k in range(len(temp)):
        s = s + int(all[k][int(temp[k])])
    if s == 0:
        res = res + 1
print(res)