inp = eval(input())
res = -1
x=0
y=0
if inp[0][0]=='1':
    for i in range(len(inp)):
        for j in range(len(inp)):
            if inp[i][j]!=inp[0][0]:
                res=i+j
                x=i
                y=j
    for i in range(len(inp)):
        for j in range(len(inp)):
            if inp[i][j]!=inp[x][y]:
                res=min(i+j,res)
else:
    for i in range(len(inp)):
        for j in range(len(inp)):
            if inp[i][j]!=inp[0][0]:
                res=i+j

if res==3:
    print(2)
else:
    print(res)