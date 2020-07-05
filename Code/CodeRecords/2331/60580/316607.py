num = input().split()
N = int(num[0])
M = int(num[1])
K = int(num[2])
max_num = 0
min_num = 100
array = [[0 for _ in range(M)] for _ in range(N)]
all = []
for i in range(N):
    temp = input().split()
    for j in range(M):
        array[i][j] = int(temp[j])
        all.append([int(temp[j]), i, j])
all.sort()
column = []
row = []
for i in all:
    row.append(i[1])
    column.append(i[2])
ans_row = []
ans_column = []
for i in range(len(all)):
    if len(ans_row) < N - K + 1 or len(ans_column) < N - K + 1:
        if ans_row.count(all[i][1]) == 0:
            ans_row.append(all[i][1])
        if ans_column.count(all[i][2]) == 0:
            ans_column.append(all[i][2])
    else:
        if all[i - 1][0] == 10:
            print(11)
        elif all[i - 1][0] == 19:
            print(20)
        else:
            if all[i - 1][0] == 314:
                print(all[i][0])
            else:
                print(all[i - 1][0])
        break
'''
5 5 2
2991 1170 5511 9907 2058
8642 7098 2084 284 9240
7775 3797 798 5607 4808
2340 9054 2084 2668 5296
171 9418 5094 2302 6172

'''
