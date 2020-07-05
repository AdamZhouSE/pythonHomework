
class Solution :
    def matrixSort(self):
        matrix = list(input())
        len = matrix[0].__len__()
        hen = matrix.__len__()
        for i in range(hen-1) :
            for o in range(len-1) :
                x0 = i
                y0 = o
                x = x0+1
                y = y0+1
                while x < hen and y < len :
                    if (matrix[x][y] < matrix[x0][y0]) :
                        matrix[x][y], matrix[x0][y0] = matrix[x0][y0], matrix[x][y]
                    x += 1
                    y += 1
        print(matrix)
so = Solution()
so.matrixSort()