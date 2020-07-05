
import sys
import collections
from typing import List
import collections
def shortestPath(grid: List[List[int]], k: int) -> int:
    m, n = len(grid), len(grid[0])
    if m == 1 and n == 1:
        return 0

    visited=[[[False]*(k+1) for _ in range(n)]for __ in range(m)]#生成三维布尔数组
    #使用队列
    visited[0][0][0]=True
    q=collections.deque([(0,0,0)])#起点坐标和已经消除的障碍个数形成三维元组
    dist=0
    while len(q)>0:
        dist+=1
        for _ in range(len(q)):
            i,j,used=q.popleft()
            #找到障碍物
            if i == m - 1 and j == n - 1:
                return dist - 1
            #没找到障碍物 四个方向移动
            for x_off,y_off in [(0,-1),(0,1),(-1,0),(1,0)]:
                x=i+x_off
                y=j+y_off
                if x<0 or x>=m or y<0 or y>=n:
                    continue
                #当前点有障碍物
                if grid[x][y]==1:
                    #还可以继续消除的情况
                    if used<k:
                        used=used+1
                        q.append([x,y,used])#
                        visited[x][y][used]=True#
                    else:#已经消除k个障碍物了，不能处理这个点的障碍物了
                         continue

                #当前点没有障碍物
                else:
                    if not visited[x][y][used]:
                        q.append([x,y,used])
                        visited[x][y][used]=True

    return -1


if __name__=="__main__":
    a=input()
    data=[]
    data.append(a[2:len(a)-2].split(","))
    while a[-1]!=']':
        a = input()
        data.append(a[2:-2].split(","))#原来可以这样写啊
    k=int(input())
    for i in range(len(data)):
        for j in range(len(data[0])):
            data[i][j]=int(data[i][j])
    ans=shortestPath(data,k)
    print(ans)