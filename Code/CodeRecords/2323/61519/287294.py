A=list(input().split(","))
k=int(input())
n=k*2
for i in range(len(A)):
    A[i]=int(A[i])
res=max(A)-min(A)-n
if(len(A)==1):
    print("0")
elif(res<=0):
    print("0")
else:
    print(res)