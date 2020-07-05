class Solution:
    def find(self, d, ords):
        d.sort()
        for o in ords:
            if o[0]==1:
                print(d[len(d)-o[1]])
            elif o[0]==2:
                i = 0
                while d[i]<o[1]:
                    i+=1
                d = d[:i]+[o[1]]+d[i:]




if __name__ == '__main__':
    [m, q] = [int(a) for a in input().split()]
    diamonds = [int(a) for a in input().split()]
    ords = []
    for i in range(q):
        ords.append([int(a) for a in input().split()])
    s = Solution()
    res = s.find(diamonds, ords)