line = input().split(' ')
nA = int(line[0])
nB = int(line[1])
line = input().split(' ')
k = int(line[0])
m = int(line[1])
A = list(map(int,input().split(' ')))
B = list(map(int,input().split(' ')))
if k>len(A) or m>len(B):
    print('NO')
else:
    A.sort()
    B.sort()
    a = A[k-1]
    b = B[len(B)-m]
    if a<b:
        print('YES')
    else:
        print('NO')