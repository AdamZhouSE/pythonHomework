class Solution:
    def find(self, n, a, b):
        for i in range(n):
            for j in range(i,n):
                if a[i]<a[j] and b[i]>b[j]:
                    return 'Happy Alex'
                elif a[i]>a[j] and b[i]<b[j]:
                    return 'Happy Alex'
        return 'Poor Alex'


if __name__ == '__main__':
    n = int(input())
    data1 = []
    data2 = []
    for i in range(n):
        line = [int(a) for a in input().split()]
        data1.append(line[0])
        data2.append(line[1])
    s = Solution()
    re = s.find(n, data1, data2)
    print(re)
