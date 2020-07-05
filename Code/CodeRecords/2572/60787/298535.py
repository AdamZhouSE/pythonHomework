l,t,o=map(int,input().split())
board=[1 for i in range(0,l)]
for step in range(0,o):
    temp=input().split()
    if temp[0]=="C":
        a,b,c=int(temp[1]),int(temp[2]),int(temp[3])
        for i in range(min(a,b)-1,max(a,b)):
            board[i]=c
    else:
        a,b=int(temp[1]),int(temp[2])
        re=[]
        for i in range(min(a,b)-1,max(a,b)):
            if not board[i] in re:
                re.append(board[i])
        print(len(re))