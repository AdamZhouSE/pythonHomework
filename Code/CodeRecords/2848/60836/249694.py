"""
给定两个数组 A 和 B，由整数组成，按非递减顺序排序
请检查是否可以在数组 A 中选择 k 个数字，在数组 B 中选择 m 个数字
使得数组 A 中所选数字都严格小于数组 B 中所选数字
"""

a=str(input())
KM=str(input()).split(" ")
k=int(KM[0])
m=int(KM[1])
A=str(input()).split(" ")
B=str(input()).split(" ")

resultA=[]
resultB=[]
while k>0:
    resultA.append(min(A))
    del A[A.index(min(A))]
    k=k-1
while m>0:
    resultB.append((max(B)))
    del B[B.index(max(B))]
    m=m-1

if max(resultA)<min(resultB):
    print("YES")
else:
    print("NO")