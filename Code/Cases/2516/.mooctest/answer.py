class Solution:
    def findRightInterval(self, intervals):
        first = [i[0] for i in intervals]
        last = [i[1] for i in intervals]
        first = sorted(enumerate(first), key = lambda x:x[1])
        last = sorted(enumerate(last), key = lambda x:x[1])
        out = [-1] * len(intervals)
        i, j = 0, 0
        while i < len(first):
            while j < len(first):
                if last[i][1] <= first[j][1]:
                    out[last[i][0]] = first[j][0]
                    break
                else:
                    j += 1
            if j >= len(first):
                break
            else:
                i += 1
        return out
num = int(input().strip())
n = []
for i in range(num):
    b = input().split(',')
    c = []
    for i in b:
        c.append(int(i))
    n.append(c)
s = Solution()
print(s.findRightInterval(n))
