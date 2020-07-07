class Solution(object):
    def reachingPoints(self, sx, sy, tx, ty):
        """
        :type sx: int
        :type sy: int
        :type tx: int
        :type ty: int
        :rtype: bool
        """
        while sx <= tx and sy <= ty:
            if sx == tx and sy == ty:
                return True
            if tx >= ty:
                tx = tx - max(ty * ((tx - sx) / ty), ty)
            else:
                ty = ty - max(tx * ((ty - sy) / tx), tx)
        return False
a = int(input())
b = int(input())
c = int(input())
d = int(input())
s = Solution()
print(s.reachingPoints(a,b,c,d))
