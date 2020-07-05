def addOne(dicc:dict,n:int):
    if n not in dicc:
        dicc[n] = 1
    else:
        dicc[n]+=1


N,K = [int(x) for x in input().split()]
current = 0
dic = dict()
for i in range(N):
    move = input().split(" ")
    step = int(move[0])
    dir = move[1]
    if(dir=="R"):
        for j in range(1,step+1):
            addOne(dic,current+j)
        current = current+step
    else:
        for j in range(1,step+1):
            addOne(dic,current-j)
        current = current-step
res  =0
for i in dic:
    if dic[i]>=K:
        res+=1
print(res)