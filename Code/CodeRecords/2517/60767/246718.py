def getSolution(A,B,C,D):
    #print("A:",A)
    #print("B:",B)
    #print("C:",C)
    #print("D:",D)
    cnt = 0
    le = len(A)
    #print("l",le)
    for i in range(0,le):
        for j in range(0,le):
            for k in range(0,le):
                for l in range(0,le):
                    #print("A[i]+B[j]+C[k]+D[l]=",A[i],"+",B[j],"+",C[k],"+",D[l],"=",A[i]+B[j]+C[k]+D[l])
                    if(A[i]+B[j]+C[k]+D[l]==0):
                        cnt += 1
    return cnt

inp = input().split(",")
A = []
for i in inp:
    A.append(int(i))
inp = input().split(",")
B = []
for i in inp:
    B.append(int(i))
inp = input().split(",")
C = []
for i in inp:
    C.append(int(i))
inp = input().split(",")
D = []
for i in inp:
    D.append(int(i))
print(getSolution(A,B,C,D))
