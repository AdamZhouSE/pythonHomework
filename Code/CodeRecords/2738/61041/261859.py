matrix = []
no = input()
while True:
    c = input()
    if c==']':
        break
    if c[len(c)-1]==',':
        c = eval(c[:len(c)-1])
    else:
        c = eval(c[:len(c)])
    matrix.append(c)
length = []
for i in range(0,len(matrix)):
    temp = []
    for j in range(0,len(matrix[0])):
        cnt = 0
        if matrix[i][j]=='0':
            temp.append(0)
        else:
            for k in range(i,len(matrix)):
                if matrix[k][j]=='1':
                    cnt+=1
                else:
                    break
            temp.append(cnt)
    length.append(temp)
max = 0
width = 1
for x in range(0,len(length)):
    for y in range(0,len(length[0])):
        if length[x][y]==0:
            continue
        else:
            for z in range(y+1,len(length[0])):
                if length[x][z]!=0 and length[x][z]>=length[x][y]:
                    width+=1
                else:
                    break
            if max<length[x][y]*width:
                max = length[x][y]*width
            width = 1
print(max)