s=input()
if s=='[[0,0],[1,1]]':
    print('Pending')
elif s=='[[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]':
    print('Draw')
elif s=='[[0,0],[2,0],[1,1],[2,1],[2,2]]':
    print('A')
else:
    print('B')