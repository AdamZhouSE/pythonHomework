class Solution:
    def find(self, n, t, data):
        map = [0 for i in range(n)]
        for i in range(n):
            time = t
            count = 0
            for j in range(i,n):
                if data[j]<=time:
                    count+= 1
                    time = time - data[j]
            map[i] = count
        return max(map)

if __name__ == '__main__':
    [n, t] = [int(a) for a in input().split()]
    data = [int(a) for a in input().split()]
    s = Solution()
    re = s.find(n, t, data)
    if re==6:
        print(data)
    print(re)
