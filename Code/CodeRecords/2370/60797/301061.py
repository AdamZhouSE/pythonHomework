class Solution:
    def find(self, n):
        re = []
        while n!=0:
            s = n//-2
            r = n % -2
            if r==-1: # n满足>0
                s+=1
                r=0
            re = re + [r]
            n = s
        return str(re.reverse())


if __name__ == '__main__':
    n = int(input())
    s = Solution()
    re = s.find(n)
    print(re)
