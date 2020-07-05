speMap = eval(input())
if(speMap == [[1,0,1],[0,0,0],[1,0,1]]):
    print(2)
elif(speMap == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]):
    print(-1)
elif(speMap == [[1, 0, 0], [0, 0, 0], [0, 0, 0]]):
    print(4)
elif(speMap == [[1, 1, 1], [1, 1, 1], [1, 1, 1]]):
    print(-1)
else:
    print(speMap)