import collections

class Solution:
    def find(self, d):
        
        r, c = len(d), len(d[0])
        data = collections.defaultdict(list)

        for i in range(r):
            for j in range(c):
                data[i - j].append(d[i][j])

        for i in data:
            data[i].sort()

        for i in range(r):
            for j in range(c):
                d[i][j] = data[i - j].pop(0)
        return d


if __name__ == '__main__':
    data = input().strip('[]').split('],[')
    for item in data:
        item = [int(a) for a in item.split(',')]
    s = Solution()
    re = s.find(data)
    print(re)

