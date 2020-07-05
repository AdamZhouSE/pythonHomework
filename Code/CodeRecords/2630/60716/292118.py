def swimInWater(grid:list()) -> int:
        import heapq
        length = len(grid)
        mark = [[0 for _ in range(length)] for _ in range(length)]
        heap = [(grid[0][0], 0, 0)]
        mark[0][0] = 1
        hmax=0
        while heap:
            h, i, j = heapq.heappop(heap)
            for x, y in ((i+1,j), (i,j+1), (i-1,j), (i,j-1)):
                if -1 < x < length and -1 < y < length and mark[x][y] == 0:
                    mark[x][y] = 1
                    if h > hmax:
                        hmax=h
                    if mark[length-1][length-1] == 1:
                        return max(grid[x][y], hmax)
                    heapq.heappush(heap, (grid[x][y], x, y))
lists = list(eval(input()))
index = swimInWater(lists)
print(index)