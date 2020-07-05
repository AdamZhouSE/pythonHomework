from queue import Queue
class Node:
    def __init__(self, value, leftchild=None, rightchild=None):
        self.leftchild = leftchild
        self.rightchild = rightchild
        self.value = value


def createTree(arr, root):
    if(root == None):
        return
    if(arr[root.value][0]!=0):
        root.leftchild = Node(arr[root.value][0])
        createTree(arr, root.leftchild)
    if (arr[root.value][1] != 0):
        root.rightchild = Node(arr[root.value][1])
        createTree(arr, root.rightchild)

def printByLevel(root):
    if(root == None):
        return
    q = Queue()
    q.put(root)
    level = 1
    print("Level",level,": ",end="")
    level += 1
    last = root
    while(q.empty()==False):
        root = q.get()
        if(root == last):
            print(root.value,end="")
        else:
            print(root.value,"",end="")
        if(root.leftchild!=None):
            q.put(root.leftchild)
            nlast = root.leftchild
        if(root.rightchild!=None):
            q.put(root.rightchild)
            nlast = root.rightchild
        if(root == last and q.empty()==False):
            print()
            print("Level",level,": ",end="")
            level += 1
            last = nlast
    return

def printByZigZag(root):
    if (root == None):
        return
    q = Queue()
    q.put(root)
    level = 1
    print("Level",level,"from left to right: ",end="")
    level += 1
    last = root
    temp = []
    judge = False
    while(q.empty()==False):
        root = q.get()
        temp.append(root)
        if (root.leftchild != None):
            q.put(root.leftchild)
            nlast = root.leftchild
        if (root.rightchild != None):
            q.put(root.rightchild)
            nlast = root.rightchild
        if (root == last and q.empty() == False):
            if(judge):
                for i in range(len(temp)-1,0,-1):
                    print(temp[i].value,"",end="")
                print(temp[0].value,end="")
                judge = False
            else:
                for i in range(0,len(temp)-1):
                    print(temp[i].value,"",end="")
                print(temp[-1].value,end="")
                judge = True
            temp = []
            print()
            if(judge==False):
                print("Level",level,"from left to right: ",end="")
            else:
                print("Level", level, "from right to left: ", end="")
            level += 1
            last = nlast
    if (judge):
        for i in range(len(temp) - 1, 0, -1):
            print(temp[i].value, "", end="")
        print(temp[0].value, end="")
        judge = False
    else:
        for i in range(0, len(temp) - 1):
            print(temp[i].value, "", end="")
        print(temp[-1].value, end="")
        judge = True






temp = input().split()
n = int(temp[0])
rootvalue = int(temp[1])
root = Node(rootvalue)
arr = [[0]*2 for i in range(111)]
for i in range(n):
    temp = input().split()
    arr[int(temp[0])][0] = int(temp[1])
    arr[int(temp[0])][1] = int(temp[2])
createTree(arr,root)
printByLevel(root)
print()
printByZigZag(root)
print()

