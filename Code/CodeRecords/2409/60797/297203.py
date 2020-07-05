class Solution:
    def find(self, data):
        odd = 0
        even = 0
        for i in range(len(data)):
           if data[i]%2==0:
               even += 1
           else:
               odd += 1
        if odd!=even:
            return min(odd,even)
        else:
            return 0

if __name__ == '__main__':
    data = [int(a) for a in input().split(',')]
    s = Solution()
    re = s.find(data)
    print(re)
