"""
给定一个整数数组 A，对于每个整数 A[i]，我们可以选择 x = -K 或是 x = K，并将 x 加到 A[i] 中
在此过程之后，我们得到一些数组 B
返回 B 的最大值和 B 的最小值之间可能存在的最小差值
"""

A=[int(i) for i in str(input()).split(",")]
K=int(input())

A.sort()

B=[]
B.append(A[0]+K)
B.append(A[len(A)-1]-K)
i=1
while(i<len(A)-1):
    b1=A[i]+K
    b2=A[i]-K
    cmp1=min(abs(b1-max(B)),abs(b1-min(B)))
    cmp2=min(abs(b2-max(B)),abs(b2-min(B)))
    if(cmp1>cmp2):
        B.append(b2)
    else:
        B.append(b1)
    i+=1

if(K==0):
    result=max(A)-min(A)
elif(len(A)==1):
    result=0
elif(A.count(A[0])==len(A)):
    result=0
else:
    result=max(B)-min(B)

print(result)