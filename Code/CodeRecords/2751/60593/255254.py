import sys
matrix=[]
lines=sys.stdin.readlines()
for i in lines:
    line=i.strip()
    matrix.append(list(line.split()))
print(matrix)