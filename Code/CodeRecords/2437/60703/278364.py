def addOne(dicc:dict,n:int):
    if n not in dicc:
        dicc[n] = 1
    else:
        dicc[n]+=1


N,K = [int(x) for x in input().split()]
current = 0
dic = dict()

moves = []
for i in range(N):
    move = input().split(" ")
    moves.append(move)
    step = int(move[0])
    dir = move[1]
    lastdir = ""
    if(dir=="R"):
        if lastdir==dir:
            current-=1
            lastdir = dir
        for j in range(1,step+1):
            addOne(dic,current+j)
        current = current+step
    else:
        if lastdir==dir:
            current+=1
            lastdir = dir
        for j in range(0,step):
            addOne(dic,current-j)
        current = current-step
res  =0
for i in dic:
    if dic[i]>=K:
        res+=1
# print(res)
# if(res == 2):
#     print(3,end="")
#     print(moves)
#     print(dic)


print(res,end="")