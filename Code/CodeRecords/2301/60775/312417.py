class Node:
    def __init__(self):
        self.path = 0
        self.end = False
        self.map = [None]*26

def insert(root:Node,word:str):
    if word == '':
        return
    root.path += 1
    for i in range(len(word)):
        index = ord(word[i])-ord('a')
        if root.map[index] == None:
            root.map[index] = Node()
        root = root.map[index]
        root.path += 1
    root.end = True

def delete(root:Node,word:str):
    if not search(root,word):
        return
    root.path -= 1
    for i in range(len(word)):
        index = ord(word[i]) - ord('a')
        root.map[index].path -= 1
        root = root.map[index]
    if root.path == 0:
        root.end = False

def search(root:Node,word:str):
    if word == '':
        return False
    for i in range(len(word)):
        index = ord(word[i]) - ord('a')
        if root.map[index] is None:
            return False
        root = root.map[index]
    return root.end

def times(root:Node,word:str):
    if word == '':
        return 0
    for i in range(len(word)):
        index = ord(word[i]) - ord('a')
        if root.map[index] is None:
            return 0
        root = root.map[index]
    return root.path


T = int(input())
root = Node()
for t in range(T):
    in1 = input().split(' ')
    opt = int(in1[0])
    word = in1[1]
    if opt == 1:
        insert(root,word)
    elif opt == 2:
        delete(root,word)
    elif opt == 3:
        print('YES' if search(root,word) else 'NO')
    elif opt == 4:
        print(times(root,word))
