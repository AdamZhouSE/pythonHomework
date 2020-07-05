a=int(input())

class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        binnum=str(bin(n)).replace('0b','')
        for i in range(len(binnum)-1):
            if abs(int(binnum[i])-int(binnum[i+1]))!=1:
                return False
        return True

b=Solution()
print(b.hasAlternatingBits(a))