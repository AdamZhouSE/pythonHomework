a=int(input())
b=int(input())
c=int(input())


class Solution:
    def numMovesStones(self, a: int, b: int, c: int):
        a, b, c = min(a,b,c), a+b+c-min(a,c,b)-max(a,b,c), max(a,b,c)
        return [min(c-a-2, (b-a>2)+1, (c-b>2)+1), c-a-2]





d=Solution()
print(d.numMovesStones(a,b,c))