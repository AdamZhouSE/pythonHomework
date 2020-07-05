"""
约翰带着奶牛去都市观光。在落日的余晖里，他们看到了一幢接一幢的摩天高楼的轮廓在地平线上形成美丽的图案
以地平线为 X 轴，每幢高楼的轮廓是一个位于地平线上的矩形，彼此间可能有 重叠的部分
奶牛一共看到了 N 幢高楼，第 i 幢楼的高度是 Hi，两条边界轮廓在地平线上的坐标是 Ai 到 Bi
请帮助奶牛们计算一下，所有摩天高楼的轮廓覆盖的总面积是多少
有一个数列，初始值均为0，他进行N次操作，每次将数列[ai,bi)这个区间中所有比Hi小的数改为Hi，他想知道N次操作后数列中所有元素的和
"""

N=int(input())

arr=[]
for i in range(N):
    arr.append([int(m) for m in str(input()).split(" ")])

building=[int(0) for i in range(1000)]
for i in range(N):
    a=arr[i][0]
    b=arr[i][1]
    h=arr[i][2]
    while(a<b):
        if(building[a]<h):
            building[a]=h
        a+=1

print(sum(building))