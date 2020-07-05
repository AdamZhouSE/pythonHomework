num=input().split()
n=input().split()
len1=int(num[0])
len2=int(num[1])
k=int(n[0])
m=int(n[1])
A=input().split()
B=input().split()
for i in range(0,len1):
    A[i]=int(A[i])
for i in range(0,len2):
    B[i]=int(B[i])
for i in range(0,len(A)):
    for j in range(0,len(A)-1):
        if A[j]>A[j+1]:
            temp=A[j]
            A[j]=A[j+1]
            A[j+1]=temp
for i in range(0,len(B)):
    for j in range(0,len(B)-1):
        if B[j]<B[j+1]:
            temp=B[j]
            B[j]=B[j+1]
            B[j+1]=temp
num1=A[k-1]
num2=B[m-1]
if num1<num2:
    print('YES')
else:
    print('NO')
