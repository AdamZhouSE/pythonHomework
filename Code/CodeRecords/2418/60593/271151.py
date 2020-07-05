class Solution(object):
    def numOfBurgers(self, tomatoSlices, cheeseSlices):
        """
        :type tomatoSlices: int
        :type cheeseSlices: int
        :rtype: List[int]
        """
        if tomatoSlices < 2*cheeseSlices or tomatoSlices > 4*cheeseSlices or (tomatoSlices & 1):
            return []

        y = (tomatoSlices  - 2*cheeseSlices)//2
        x = cheeseSlices - y
        if x*2 + y*4 == tomatoSlices:
            return [y,x]
        return []
x=int(input())
y=int(input())
print(Solution().numOfBurgers(x,y))