m,n=map(int,input().split())
rows=[]
for i in range(m):
    rows.append(input())
row=[]
column=[]
for i in range(len(rows)):
    if('B'in rows[i]):
        row.append(i)
for i in range(n):
    for j in range(m):
        if rows[j][i]=='B' and i not in column:
            column.append(i)
print(row[int(len(row)/2)]+1,column[int(len(row)/2)]+1)