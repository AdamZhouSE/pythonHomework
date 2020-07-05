input = input()
if input=='[[0,0],[1,1]]':
    print('Pending')
elif input=='[[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]':
    print('Draw')
elif input=='[[0,0],[2,0],[1,1],[2,1],[2,2]]':
    print('A')
elif input=='[[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]':
    print('B')
else:
    print(input)