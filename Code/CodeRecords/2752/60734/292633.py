import re
from collections import namedtuple
def isConneted(x1,y1,x2,y2):
    '''
    判断地图上两个点是否连通
    :param x1:
    :param y1: 起始坐标
    :param x2:
    :param y2: 终点坐标
    :return:
    '''
    queue = [(x1,y1)]
    while queue:
        begin = queue.pop(0)
        notvisited[begin[0]][begin[1]] = False
        if begin[0] == x2 and begin[1] == y2:
            return True
        dirs = [[-1,0], [1,0], [0,-1], [0,1]]
        for dir in dirs:
            next = [begin[0]+dir[0],begin[1]+dir[1]]
            if 0<=next[0]<len(matrix) and 0<=next[1]<len(matrix[0]) \
                    and matrix[next[0]][next[1]]!=0 \
                    and notvisited[next[0]][next[1]]:
                queue.append(next)
        '''
        # up
        if begin[0]-1>0 and matrix[begin[0]-1][begin[1]] != 0 and notvisited[begin[0]-1][begin[1]]:
            queue.append((begin[0]-1,begin[1]))
        # down
        if begin[0]+1<len(matrix) and matrix[begin[0]+1][begin[1]] != 0 and notvisited[begin[0]+1][begin[1]]:
            queue.append((begin[0]+1,begin[1]))
        # left
        if begin[1]-1>0 and matrix[begin[0]][begin[1]-1] != 0 and notvisited[begin[0]][begin[1]-1]:
            queue.append((begin[0],begin[1]-1))
        # right
        if begin[1]+1<len(matrix[0]) and matrix[begin[0]][begin[1]+1] != 0 and notvisited[begin[0]][begin[1]+1]:
            queue.append((begin[0],begin[1]+1))
        '''
    return False

# input

matrix = []

for line in iter(input, ']'):
    if line != '[':
        lst = list(map(int, re.findall(r'\d+', line)))
        matrix.append(lst)
'''
matrix = [[1,2,3],
          [0,0,4],
          [7,6,5]]
'''
trees = []
tree = namedtuple('tree',['x','y','h'])
for row in range(len(matrix)):
    for col in range(len(matrix[0])):
        if matrix[row][col]>0:
            trees.append(tree(row,col,matrix[row][col]))

trees = sorted(trees,key=lambda x: x.h)

step = 0

notvisited = [[True]*len(matrix[0]) for i in range(len(matrix))]
begin = [0,0]
for t in trees:
    if isConneted(begin[0],begin[1],t.x,t.y):
        step+=abs(t.x-begin[0])+abs(t.y-begin[1])
        begin = [t.x,t.y]
    else:
        step = -1
        break
print(step)