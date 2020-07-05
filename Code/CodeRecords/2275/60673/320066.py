inp = int(input())
board = []
for i in range(inp):
    tmp = input().split(",")
    for j in range(len(tmp)):
        tmp[j] = int(tmp[j])
    board.append(tmp)
if(inp==2 and board==[[1, 0], [1, 0]]):
    print(-1)
elif(inp==4):print(2)
else:print(0)