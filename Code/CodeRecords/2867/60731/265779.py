matrix=[[]]
line1=0
column1=0
for i in range(5):
    line=input().split()
    if '1' in line:
        line1=i+1
        for j in range(5):
            if line[j]=='1':
                column1=j+1
    matrix.append(line)
res=abs(line1-3)+abs(column1-3)
print(res)