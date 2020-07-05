import operator
class Solution(object):
    def canTransform(self, start, end):
        if start.replace('X','') != end.replace('X', ''):
            return False

        for (symbol, op) in (('L', operator.ge), ('R', operator.le)):
            B = (i for i, c in enumerate(end) if c == symbol)
            for i, c in enumerate(start):
                if c == symbol and not op(i, next(B)):
                    return False

        return True
s=input()
r=input()
print(Solution().canTransform(s,r))