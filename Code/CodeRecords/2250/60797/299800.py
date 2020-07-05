class Solution:
    def find(self, n, points):
        if n <= 2:
            return n

        max = 2
        for i in range(0, n):
            samePosition = 0 # 重复位置的点个数
            sameSlope = 1 # 斜率相同的点个数
            for j in range(i + 1, n):
                x1 = points[j][0] - points[i][0]
                y1 = points[j][1] - points[i][1]
                if x1 == 0 and y1 == 0:
                    samePosition+=1
                else:
                    sameSlope+=1 # 第二个点，所以可以直接++
                for k in range(j + 1, n):
                    x2 = points[k][0] - points[i][0]
                    y2 = points[k][1] - points[i][1]
                    if x1 * y2 == x2 * y1:
                        sameSlope+=1
                if max < (samePosition + sameSlope):
                    max = samePosition + sameSlope
                sameSlope = 1
        return max


if __name__ == '__main__':
    n = int(input())
    data=[]
    for i in range(n):
        line = [int(a) for a in input().split(',')]
        data.append(line)
    s = Solution()
    re = s.find(n, data)
    print(re)