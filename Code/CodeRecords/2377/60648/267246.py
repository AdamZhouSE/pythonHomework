from typing import List
class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        return (points[0][0] - points[1][0]) * (points[0][1] - points[2][1]) - (points[0][1] - points[1][1]) * (points[0][0] - points[2][0]) != 0


if __name__=="__main__":
    n=int(input())
    ls=[]
    for i in range(n):
        s=input().split(',')
        s=[int(s[i]) for i in range(len(s))]
        ls.append(s)
    x=Solution().isBoomerang(ls)
    print(x)