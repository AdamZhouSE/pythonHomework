length = int(input())
A = [int(i) for i in input().split()]
mina = A[0]
result = 1
for i in range(len(A)):
	if(mina > A[i]):
		mina = A[i]
for i in range(len(A)):
	if(A[i] % mina != 0):
		result = 0
		break
	
if(result == 0):
	print(-1)
else:
	print(mina)
