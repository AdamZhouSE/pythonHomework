n = int(input())
M = []
for i in range(n):
    M.append([int(x) for x in input().split(",")])
k = int(input())
prefix = [[0 for y in range(len(M[0]))] for x in range(len(M))]
for x in range(len(M)):
    prefix[x][0] = M[x][0]
for x in range(len(M)):
    for y in range(1, len(M[0])):
        prefix[x][y] = prefix[x][y - 1] + M[x][y]
res = 0
for left in range(len(M[0])):
    for right in range(left, len(M[0])):
        area = []
        pre_area = 0
        for i in range(len(M)):
            cur_area = 0
            if left == 0:
                cur_area = prefix[i][right] + pre_area
            else:
                cur_area = prefix[i][right] - prefix[i][left-1] + pre_area
            newarea = area.copy()
            newarea.sort()
            x = 0
            while x < len(newarea) and newarea[x] < cur_area - k:
                x += 1
            if x != len(newarea):
                res = max(res, cur_area - newarea[x])
            area.append(cur_area)
            pre_area = cur_area
        #print(area)
#print(prefix)
print(res)
