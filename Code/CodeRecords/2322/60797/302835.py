import math


class Solution:
    def isPalindrome(self, ss):
        for i in range(len(ss)):
            if ss[i]!=ss[len(ss)-i-1]:
                return False
            if i == len(ss)-i-1:
                break
        return True

    def find(self, l,r):
        count = 0
        for i in range(l, r+1):
            if self.isPalindrome(str(i)) and self.isPalindrome(str(math.sqrt(i))):
                count +=1
        return count




if __name__ == '__main__':
    l = int(input())
    r = int(input())
    s = Solution()
    re = s.find(l,r)
    print(re)