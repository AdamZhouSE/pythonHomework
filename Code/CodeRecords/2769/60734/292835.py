def length(x1,y1,x2,y2,rest):
    notvisited = [[True] * len(matrix[0]) for i in range(len(matrix))]
    queue = [[x1,y1,rest]]
    step = 0
    while queue:
        q_s = len(queue)
        while q_s>0:
            begin = queue.pop(0)
            x,y = begin[0],begin[1]
            q_s -= 1
            notvisited[x][y] = False
            if x == x2 and y == y2:
                return step
            for dx,dy in [[1,0], [0,1], [-1,0], [0,-1]]:
                nx, ny = x+dx, y+dy
                # 无障碍 正常迭代
                if 0<=nx<len(matrix) and 0<=ny<len(matrix[0]) \
                        and matrix[nx][ny]!=1 \
                        and notvisited[nx][ny]:
                    queue.append([nx,ny])
                # 有障碍 rest-1继续迭代
                elif 0<=nx<len(matrix) and 0<=ny<len(matrix[0]) \
                        and matrix[nx][ny] == 1 \
                        and notvisited[nx][ny] and rest>0:
                    queue.append([nx,ny])
                    rest-=1
        step += 1
    return -1  # 表示不连通

import re
#input
matrix = []
for line in iter(input,''):
    matrix.append(list(map(int,re.findall(r'\d+',line))))
    if line.endswith(']'):
        break
k = int(input())
'''
matrix = [[0,0,0],
          [1,1,0],
          [0,0,0],
          [0,1,1],
          [0,0,0]]
k=1
'''

print(length(0,0,len(matrix)-1, len(matrix[0])-1,k))