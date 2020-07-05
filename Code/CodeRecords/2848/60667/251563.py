first = input().split()
nA = int(first[0])
nB = int(first[1])
second = input().split()
k = int(second[0])
m = int(second[1])
A = list(map(int,input().split()))
B = list(map(int,input().split()))
    
if A[k-1] < B[len(B)-m]:
     print('YES')
else:
     print('NO')    