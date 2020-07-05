class Solution:
    def find(self, d):
        
        r, c = len(d), len(d[0])
        data = []

        for i in range(r):
            for j in range(c):
                data[i - j].append(d[i][j])

        for item in data:
            item.sort()

        for i in range(r):
            for j in range(c):
                d[i][j] = data[i - j].pop(0)
        return d


if __name__ == '__main__':
    data = [int(a) for a in input().strip('[]').split('],[')]
    for item in data:
        item = item.split(',')
    s = Solution()
    re = s.find(data)
    print(re)

