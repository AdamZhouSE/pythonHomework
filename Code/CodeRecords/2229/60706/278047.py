list1=input().split(',')
A=[]
for i in range(len(list1)):
    A.append(int(list1[i]))
N = len(A)
floor = N
ans=True
for i in range(N-1, -1, -1):
    floor = min(floor, A[i])
    if i >= 2 and A[i-2] > floor:
        ans=False
print(ans)

