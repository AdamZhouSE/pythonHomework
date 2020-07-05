# LeetCode 789
import math


class Solution:
    def escapeGhosts(self, ghosts, target):
        return abs(target[0])+abs(target[1])<min([abs(target[0]-g[0])+abs(target[1]-g[1]) for g in ghosts])


count = eval(input())
ghosts = []
for i in range(count):
    line = input().split(',')
    line = [int(x) for x in line]
    ghosts.append(line)
target = input().split(',')
target = [int(x) for x in target]
s = Solution()
print(s.escapeGhosts(ghosts, target))
