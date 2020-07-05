a=int(input())
b=int(input())



class Solution:
    def brokenCal(self, x: int,y: int) -> int:

        if x>=y:
            return x-y
        if y%2==0:
            return self.brokenCal(x,y/2)+1
        else:
            return self.brokenCal(x,y+1)+1


c=Solution()
print(int(c.brokenCal(a,b)))