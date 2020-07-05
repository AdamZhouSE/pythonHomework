"""
平面上有 n 个点，你需要以 x 轴和 y 轴为两条边
做一个最小的等腰直角三角形以覆盖所有的点，请问这个三角形的最短边是多少？
"""

n=int(input())
arr=[]

for i in range(n):
    arr.append([int(m) for m in str(input()).split(" ")])

max_edge=0
for i in range(len(arr)):
    edge=arr[i][0]+arr[i][1]
    if max_edge<edge:
        max_edge=edge
        
print(max_edge)