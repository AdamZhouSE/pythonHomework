string = input().split(",")
n = len(string)
A = []
B = []
for x in string:
    if int(x) in A:
        B[A.index(int(x))] += 1
    else:
        A.append(int(x))
        B.append(1)
index = 0
while index < len(B):
    if B[index] > n/2:
        print(A[index])
    index += 1
