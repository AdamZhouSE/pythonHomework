class Solution:
    def find(self, n, data):
        re=0
        count = 0
        for item in data:
            if item>0:
                re += item - 1
            elif item<0:
                re += -1 - item
                count += 1
            else:
                re += 1
        #if count%2!=0:
            #re += 2
        return re


if __name__ == '__main__':
    n = int(input())
    data = [int(a) for a in input().split()]
    s = Solution()
    re = s.find(n, data)
    print(re)
    #if re==0:
        #print(n)
        #print(data)