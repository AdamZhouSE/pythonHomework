from typing import List
class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        n = len(points)
        all_pos = set()
        for i, j in points:
            all_pos.add((i, j))

        ans = 0x7fffffff
        for i in range(n):
            for j in range(i+1, n):
                a, b = points[j][0] - points[i][0], points[j][1] - points[i][1]
                for k in range(j+1 , n):
                    c, d = points[k][0] - points[i][0], points[k][1] - points[i][1]
                    if a*c + b*d == 0 and (points[i][0] + a+c, points[i][1] + b+d) in all_pos:
                        ans = min(ans, abs(a*d - b*c))
        return 0.0000 if ans == 0x7fffffff else ans


if __name__=="__main__":
    n=int(input())
    ls=[]
    for i in range(n):
        ls.append(eval('['+input()+']'))
    x=float(Solution().minAreaFreeRect(ls))
    if x=0.0:
        print(0.0000)
    else:
        print(x)