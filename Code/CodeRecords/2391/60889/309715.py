class Node():
    def __init__(self,data):
        self.data = data
        self.sons = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        
numOfNames = int(input())
tree = Node(0)
nowNode = tree
for i in range(numOfNames):
    name = input()
    for j in name:
        loc = ord(j)-97
        if nowNode.sons[loc] == 0:
            nowNode.sons[loc] = Node(0)
        nowNode = nowNode.sons[loc]
    nowNode.data = 1
    nowNode = tree
numOfCall = int(input())
for i in range(numOfCall):
    call = input()
    for j in call:
        loc = ord(j)-97
        if nowNode.sons[loc] == 0:
            print("WRONG")
            break
        nowNode = nowNode.sons[loc]
    else:
        if nowNode.data == 0:
            print("WRONG")
        elif nowNode.data == 1:
            print("OK")
            nowNode.data = 2
        else:
            print("REPEAT")
    nowNode = tree
            
            
            
            
            
            
            