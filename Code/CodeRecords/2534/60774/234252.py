A = input()
B = []
for i in range(0,len(A)):
    if(A[i] is '[' or A[i] is ']' or A[i] is ','):
        continue
    else:
        B.append(int(A[i]))
B = sorted(B)
print(B)