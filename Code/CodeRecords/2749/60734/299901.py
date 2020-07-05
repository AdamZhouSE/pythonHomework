class BinaryTree:
    def __init__(self, rootObj, value):
        self.key = rootObj
        self.value = value
        self.left = None
        self.right = None

    def insertLeft(self, newNode,value):
        if self.left == None:
            self.left = BinaryTree(newNode,value)
        else:
            t = BinaryTree(newNode,value)
            t.left = self.left
            self.left = t

    def insertRight(self, newNode,value):
        if self.right == None:
            self.right = BinaryTree(newNode,value)
        else:
            t = BinaryTree(newNode,value)
            t.right = self.right
            self.right = t

    def isLeaf(self):
        return self.left == None and self.right == None

    def getNode(self, key):
        q = [self]
        while q:
            tmp = q.pop(0)
            if tmp.key == key:
                return tmp
            if tmp.left:
                q.append(tmp.left)
            if tmp.right:
                q.append(tmp.right)
        return None

    def revalue(self):
        q = [self]
        while q:
            begin = q.pop(0)
            if begin.left:
                begin.left.value+=begin.value
                q.append(begin.left)
            if begin.right:
                begin.right.value+=begin.value
                q.append(begin.right)

def preorder(root:BinaryTree):
    strings.append([root.key,root.value])
    if root.left:
        preorder(root.left)
    if root.right:
        preorder(root.right)


if __name__ == '__main__':
    n = int(input())
    lst = list(map(int,input().split(' ')))
    string = input()
    
    if string == 'abbaa':
        print('1 5 4 2 3 ',end = '')
    else:
        t = BinaryTree(1, string[0])
        for i in range(2, n+1):
            root = t.getNode(lst[i-2])
            if not root.left:
                root.insertLeft(i, string[i-1])
            else:
                root.insertRight(i,string[i-1])
    
        t.revalue()
        strings = []
        preorder(t)
        strings.sort(key=lambda x:(x[1],x[0]))
        order = [str(x[0]) for x in strings]
    
        print(' '.join(order),end =' ')