m=int(input())
n=int(input())
opes=int(input())
add_rows,add_columns=[],[]
for i in range(opes):
    ope=input().split(',')
    add_rows.append(int(ope[0]))
    add_columns.append(int(ope[1]))
x=min(min(add_rows),m)
y=min(min(add_columns),n)
print(x*y)