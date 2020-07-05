class Node():
    def __init__(self,data,left=0,right=0):
        self.data = data
        self.left = left
        self.right = right
    
        
numOfNode = int(input())
nums = list(map(int,input().split(" ")))
tree = Node(nums[0])
print(-1)
del nums[0]
for i in nums:
    node = tree
    lastNode = -1
    while node != 0:
        a = 0
        lastNode = node
        if node.data>i:
            node = node.left
            a=1
        else:
            node = node.right
            a=2
    if a==1:
        lastNode.left = Node(i)
    else:
        lastNode.right = Node(i)
    print(lastNode.data)
    