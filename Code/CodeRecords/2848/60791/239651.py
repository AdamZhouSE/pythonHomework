na, nb = input().split()
k, m = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
a = A[k-1]
b = B[len(B) - m]
if(a < b):
	print('YES')
else:
	print('NO')