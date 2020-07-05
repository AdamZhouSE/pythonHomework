n = int(input())
inp = []
for i in range(n):
    li = eval(input())
    inp.append(li)
#print(inp)

class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        c=0
        for i in range(len(points)-1):
            c+=max(abs(points[i+1][0]-points[i][0]),abs(points[i+1][1]-points[i][1]))
        return c
s = Solution()
print(s.minTimeToVisitAllPoints(inp))