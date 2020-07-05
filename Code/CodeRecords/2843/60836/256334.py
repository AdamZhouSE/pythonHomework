"""
b 序列有 n 个整数 b[1], b[2], ... b[n]
定义 a[i] = b[i] - b[i+1] + b[i+2] - ... b[n]
现给定 a[1] 到 a[n] 的值，你能还原出 b 序列吗？
"""

n=int(input())
arr=[int(m) for m in str(input()).split(" ")]

B=[]
for i in range(len(arr)-1):
    B.append(arr[i]+arr[i+1])
B.append(arr[len(arr)-1])

B=[str(m) for m in B]
print(" ".join(B))