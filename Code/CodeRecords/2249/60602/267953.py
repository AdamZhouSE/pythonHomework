from typing import List
def makeIntList(list):
    count = 0;
    while (count < len(list)):
        list[count] = int(list[count]);
        count += 1;
    return list;
class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        xy = sum([sum([1 if j else 0 for j in i]) for i in grid]) #m*n
        xz = sum([max(i) for i in grid]) # m*1
        yz = sum([max([grid[i][j] for i in range(m)]) for j in range(n)]) #n*1
        #print(xy, xz, yz)
        return xy+xz+yz

Total=int(input());
i=0;
ans=[];
while(i<Total):
    temp=makeIntList(input().split(","));
    ans.append(temp);
    i+=1;
solution=Solution();
print(solution.projectionArea(ans));