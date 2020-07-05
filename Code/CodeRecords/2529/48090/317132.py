import collections
num=int(input())



class Solution:
    def reorderedPowerOf2(self, N):
        temp = []
        for i in range(31):
            temp.append(collections.Counter(str(2 ** i)))
        for each in temp:
            if collections.Counter(str(N)) == each:
                return True
        return False


c=Solution()
print(str(c.reorderedPowerOf2(num)).lower())