nums = input()[1:-1].split(',')
k = int(input())
for i in range(0, len(nums)):
    nums[i] =int(nums[i])
n = len(nums)
A = []
B = []

for i in range(0,n-1):
    for j in range(i,n):
        if nums[i]<nums[j]:
            A.append(nums[i]/nums[j])
            B.append([nums[i],nums[j]])
C =[]
for i in range(0,len(A)):
    C.append(A[i])
C.sort()
index = A.index(C[k-1])

print('[',end='')
print(B[index][0],end=', ')
print(B[index][1],end=']')
print()