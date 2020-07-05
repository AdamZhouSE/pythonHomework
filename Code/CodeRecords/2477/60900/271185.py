n = int(input())
res = []
for i in range(0,2*n):
    res.append(input().split(" "))

for i in range(0,n):
    result =0
    for j in range(0,4):
        if res[2*i][j]==res[2*i+1][j]:
            result = 1
    print(result)