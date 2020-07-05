class treeNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    def toString(self):
        if(self.left == None and self.right == None):
            return str(self.value)
        if(self.left == None):
            return str(self.value) + " " + self.right.toString()
        if(self.right == None):
            return str(self.value) + " " + self.left.toString()
        return str(self.value) + " " + self.left.toString() + " " + self.right.toString()
    def insert(self,value):
        if(self.value == None):
            self.value = value
        else:
            if(value < self.value):
                # 左侧插入
                if(self.left == None):
                    self.left = treeNode(value)
                else:
                    self.left.insert(value)
            else:
                if(self.right == None):
                    self.right = treeNode(value)
                else:
                    self.right.insert(value)


n = input()
nums = list(map(int,input().strip().split(" ")))
t = treeNode(None)

for num in nums:
    t.insert(num)
print(t.toString(),end = " ")