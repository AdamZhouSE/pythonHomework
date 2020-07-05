class Solution:
    def find(self, d):
        re = []
        d.sort()
        cur = [d[0][0],d[0][1]]
        for i in range(1,len(d)):
            if cur[1]<d[i][0]:
                re.append(cur)
                cur = [d[i][0],d[i][1]]
            else:
                cur[1] = d[i][1]
        return re


if __name__ == '__main__':
    n = int(input())
    data=[]
    for i in range(n):
        line = [int(a) for a in input().split()]
        data.append(line)
    s = Solution()
    res = s.find(data)
    for item in res:
        print(item[0],end=' ')
        print(item[1])

