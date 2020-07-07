class Solution(object):
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        for i in range(len(A)):
            if A[i] != i and abs(A[i] - i) > 1:
                return False
        return True
b = input().split(',')
c= []
for i in b:
    c.append(int(i))
s = Solution()
print(s.isIdealPermutation(c))