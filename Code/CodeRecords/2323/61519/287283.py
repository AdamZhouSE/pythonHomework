A=list(input().split(","))
k=int(input())
for i in range(len(A)):
    A[i]=int(A[i])
if(len(A)==1 | max(A)-min(A)-2*k<=0):
    print("0")
else:
    print(max(A)-min(A)-2*k)