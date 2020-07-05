num = int(input())
matrix = []
for i in range(num):
    matrix.append(input().split(","))
all = int(input())
res = []
for m in range(1,min(len(all),len(all[0]))):
    for i in range(len(all)):
        for k in range(len(all[0])):
            temp = []
            for n in range(m):
                temp.append(all[n+i][k:k+n
            if judge(     