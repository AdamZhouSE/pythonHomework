class Solution:
    def find(self, data):
        sticks = [0 for i in range(10)]
        for i in range(6):
            sticks[data[i]] += 1
        legindex = 0
        a,b = 0,0
        for i in range(10):
            if sticks[i]==1:
                if a==0:
                    a = i
                else:
                    b = i
            elif sticks[i]==6:
                return 'Elephant'
            elif sticks[i]==5:
                return 'Bear'
            elif sticks[i]==4:
                legindex = i
        if legindex==0:
            return "Alien"
        if a==b:
            return 'Elephant'
        else:
            return 'Bear'


if __name__ == '__main__':
    data = [int(a) for a in input().split()]
    s = Solution()
    re = s.find(data)
    print(re)
