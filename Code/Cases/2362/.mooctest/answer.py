from itertools import cycle
class Solution:
    def clumsy(self, N: int) -> int:
        return eval(str(N)+''.join(map(lambda a,b:a+str(b),cycle(['*','//','+','-']),range(N-1,0,-1))))


a = int(input())
s = Solution()
print(s.clumsy(a))