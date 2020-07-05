list1=input().split(',')
A=[]
for i in range(len(list1)):
    A.append(int(list1[i]))
A.sort()
ans=0
i=len(A)-3
while i>=0:
    if A[i]+A[i+1]>A[i+2]:
        ans=A[i]+A[i+1]+A[i+2]
        break
    i=i-1
print(ans)

