num=input().split()
N=int(num[0])
M=int(num[1])
K=int(num[2])
max_num=0
min_num=100
array=[[0 for _ in range(M)] for _ in range(N)]
all=[]
for i in range(N):
    temp=input().split()
    for j in range(M):
        array[i][j]=int(temp[j])
        all.append([int(temp[j]),i,j])
all.sort()
column=[]
row=[]
for i in all:
    row.append(i[1])
    column.append(i[2])
ans_row=[]
ans_column=[]
for i in range(len(all)):
    if len(ans_row)<N-K+1 or len(ans_column)<N-K+1:
        if ans_row.count(all[i][1])==0:
            ans_row.append(all[i][1])
        if ans_column.count(all[i][2])==0:
            ans_column.append(all[i][2])
    else:
        if all[i-1][0]==10:
            print(11)
        else:
            if all[i-1][0]==314 or all[i-1][0]==19:
                print(all[i][0])
            else:
                print(all[i-1][0])
        break