inp = eval(input())
res = -1
for i in range(len(inp)):
    for j in range(len(inp)):
        if inp[i][j]!=inp[0][0]:
            res=i+j
print(res)