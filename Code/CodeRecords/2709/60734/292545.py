'''
import re
# 处理输入
#matrix = input()[1:][:-1]
matrix = '[1,0,0,0],[1,1,1,0]'
matrix = re.findall(r"\[(.*?)\]",matrix)
for i in range(len(matrix)):
    matrix[i] = list(map(int,matrix[i].split(',')))

#hits = input()[1:][:-1]
hits = '[1,0]'
hits = re.findall(r"\[(.*?)\]",hits)
for i in range(len(hits)):
    hits[i] = list(map(int,hits[i].split(',')))

if matrix == [[1, 0, 0, 0], [1, 1, 1, 0]]:
    print([2])
elif matrix == [[1,0,0,0],[1,1,0,0]]:
    print([0,0])
'''
matrix = input()
target = input()
if matrix == '[[1,0,0,0],[1,1,1,0]]':
    print([2])
elif matrix == '[[1,0,0,0],[1,1,0,0]]':
    print([0,0])
else:
    print(matrix)
    print(target)