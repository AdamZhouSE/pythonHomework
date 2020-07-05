import sys

lst = []
for line in sys.stdin:
    if line.strip() == '':
        break
    lst.append(line)

total = []
i = 0
while i < len(lst[0]):
    if lst[0][i] >= '0' and lst[0][i] <= '9':
        str = lst[0][i]
        if i >= len(lst[0])-1:
            break
        while lst[0][i+1] != '\n' and lst[0][i+1] != ' ':
            str += lst[0][i+1]
            i += 1
            if i >= len(lst[0]) - 1:
                break
        total.append(str)
    i += 1
number = int(total[1]) #路线数
point = int(total[0]) #点数
begin = total[2] #起始点
ending = total[3] #目的点

had = []
for i in range(0,number):
    lined = []
    j = 0
    while j < len(lst[i+1]):
        if lst[i+1][j] >= '0' and lst[i+1][j] <= '9':
            str = lst[i+1][j]
            if j >= len(lst[i+1])-1:
                break
            while lst[i+1][j+1] != '\n' and lst[i+1][j+1] != ' ':
                str += lst[i][j+1]
                j += 1
                if j >= len(lst[i + 1]) - 1:
                    break
            lined.append(str)
        j += 1
    had.append(lined)

for i in range(0,number):
    had[i][2] = int(had[i][2])
    had.append([had[i][1],had[i][0],had[i][2]])

i = 0

while i < len(had)-1:
    j = i + 1
    while j < len(had):
        if had[i][0]==had[j][0] and had[i][1]==had[j][1]:
            if had[i][2] > had[j][2]:
                had[i] = [0,0,0]
            else:
                had[j] = [0,0,0]
        j += 1
    i += 1
while had.count([0,0,0])!=0:
    had.remove([0,0,0])
number = len(had) #有效边数，考虑短边和双向

matrix = [[ 0 for i in range(3)] for i in range(point)]
for i in range(0,point):
    matrix[i] = [begin , '%d' %(i+1) ,-1]
matrix[int(begin)-1] = [begin,begin,0]

for i in range(0,number):
   if had[i][0] == begin:
        if matrix[int(had[i][1])-1][2]==-1 or matrix[int(had[i][1])-1][2] > had[i][2]:
            matrix[int(had[i][1])-1] = had[i]
            matrix[int(had[i][1])-1][2] = int(matrix[int(had[i][1])-1][2])

count = 0
while count < point:
    for i in range(0,point):
        if matrix[i][2] != -1:
            begin = matrix[i][1]
            distance = matrix[i][2]
            for j in range(0,number):
                if had[j][0] == begin:
                    end = had[j][1]
                    lineNo = int(end) - 1
                    if matrix[lineNo][2] ==-1 or matrix[lineNo][2] > distance + had[j][2]:
                        matrix[lineNo][2] = distance + had[j][2]
    count += 1;

print(matrix[int(ending)-1][2])


