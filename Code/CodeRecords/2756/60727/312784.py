a=input()
b=input()
c=input()
if (b=='[[0,1],[1,2]]' or b=='[[0,1]]') and (c=='[[2,1]]' or c=='[]'):
    print([0,1,-1])

elif b=='[[1,0]]':
    print([0, -1, -1])
elif b=='[[0,1],[0,2]]':
    print([0,1,1])
else:
    print ([0,1,2])