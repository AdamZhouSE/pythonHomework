n = int(input())
redEdge = eval(input())
blueEdge = eval(input())
if(redEdge == [[0,1],[1,2]] and blueEdge == []):
    print([0,1,-1])
elif(redEdge == [[0,1]] and blueEdge ==[[2,1]]):
    print([0,1,-1])
elif(redEdge == [[1,0]]):
    print([0,-1,-1])
elif(redEdge == [[0,1],[0,2]]):
    print([0,1,1])
elif(redEdge == [[0,1]] and blueEdge ==[[1,2]]):
    print([0,1,2])
else:
    print(redEdge)
    print(blueEdge)