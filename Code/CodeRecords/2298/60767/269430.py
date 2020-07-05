class Node:
    def __init__(self, value, leftchild=None, rightchild=None):
        self.leftchild = leftchild
        self.rightchild = rightchild
        self.value = value


def insert(t,element,father):
    if(t==None):
        t = Node(element)
    elif(t.value<element):
        t.leftchild = insert(t.leftchild,element,father)
        father.append(t.value)
    elif(t.value>element):
        t.rightchild = insert(t.rightchild,element,father)
        father.append(t.value)
    return t


N = int(input())
temp = input().split()
t = None
for i in range(N):
    father = []
    t = insert(t,int(temp[i]),father)
    if(len(father)==0):
        print(-1)
    else:
        print(father[0])