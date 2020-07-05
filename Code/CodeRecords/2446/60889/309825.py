class Node():
    def __init__(self,data):
        self.data = data
        self.sons = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

numOfArticle = int(input())
trees = []
for i in range(numOfArticle):
    article = input().split()
    length = int(article[0])
    tree = Node(0)
    nowNode = tree
    for j in range(1,length+1):
        for k in article[j]:
            loc = ord(k)-97
            if nowNode.sons[loc] == 0:
                nowNode.sons[loc] = Node(0)
            nowNode = nowNode.sons[loc]
        nowNode.data = 1
        nowNode = tree
    trees.append(tree)
numOfWord = int(input())
for i in range(numOfWord):
    word = input()
    judge = True
    for j in range(len(trees)):
        nowNode = trees[j]
        for k in word:
            loc = ord(k)-97
            if nowNode.sons[loc] == 0:
                break
            nowNode = nowNode.sons[loc]
        else:
            if nowNode.data == 1:
                print(j+1,end=" ")
                judge = False
    if judge:
        print(" ")
    else:
        print("")