class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        p, d = 0, 1
        for i in instructions:
            d *= (i == 'G') + 1j * ((i == 'L') - (i == 'R'))
            p += d * (i == 'G')
        return p == 0 or d != 1


if __name__=="__main__":
    n=input()
    x=Solution().isRobotBounded(n)
    print(x)