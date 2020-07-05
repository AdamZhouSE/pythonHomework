def judge(l,n):
    res = 0
    for i in l:
        for k in i:
            res = res + int(k)
    return res<=n


num = int(input())
matrix = []
for i in range(num):
    matrix.append(input().split(","))
all = int(input())
res = []
for m in range(1,min(len(matrix),len(matrix[0]))+1):
    for i in range(len(matrix)-m+1):
        for k in range(len(matrix[0])-m+1):
            temp = []
            for n in range(m):
                temp.append(matrix[n+i][k:k+m])
            if judge(temp,all):
                res.append(m)
result = 0
if len(res)!=0:
    result = max(res)
print(result)
