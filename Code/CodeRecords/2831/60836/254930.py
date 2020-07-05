"""
某地铁环线有 n 个车站。 我们知道所有邻近站点之间的距离：
d[1] 是第 1 站和第 2 站之间的距离;
d[2] 是第 2 站和第 3 站之间的距离;
......
d[n-1] 是第 n-1 和第 n 个站之间的距离;
d[n]是第 n 个站和第 1 个站之间的距离。
列车沿着两个方向的环线。 找到站点 s 和 t 之间的最短距离
"""

n=int(input())
arr=[int(m) for m in str(input()).split(" ")]
NM=str(input()).split(" ")
s=int(NM[0])
t=int(NM[1])

if s>t:
    a=s;s=t;t=a

distance1=0
distance2=0
while s<t:
    distance1=distance1+arr[s-1]
    s=s+1
distance2=sum(arr)-distance1

print(min(distance1,distance2))