l=input().split(',')
if len(l)!=3:
    print(False)
else:
    board=[]
    for i in range(3):
        temp=list(l[i])
        board.append(temp)
    
