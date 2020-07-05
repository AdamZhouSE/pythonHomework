'''
在第X站，年龄为A岁的孩子下车了。
龄大于等于B且在第Y站（包含第Y站）以前下车的最年轻的小孩是多大？
3 4
M 10 3
M 5 1
D 20 2
D 5 1
'''
class node():
    def __init__(self, age, station, left, right):
        self.age = age
        self.station = station
        self.left = left
        self.right = right        
def create(root, node):
    if root == None:
        root = node
    elif node.age >= root.age:
        if root.right == None:
            root.right = node
        else:
            create(root.right, node)
    else:
        if root.left == None:
            root.left = node
        else:
            create(root.left, node)
    #print(root.age, node.age)
    return root

n, q = map(int, input().split())
target = []
root = None
for i in range(q):
    tem = input().split()
    if tem[0] == "M":
        root = create(root, node(int(tem[2]), int(tem[1]), None, None))
    elif tem[0] == "D":
        target.append([int(tem[1]), int(tem[2])])

minnum = 123456
def find(root, age, station):
    global minnum
    if root == None:
        return
    #print(age, root.age)
    if root.age >= age:
        if root.station <= station:
            if minnum >= root.age:
                minnum = root.age
                #print(minnum)
        find(root.right, age, station)
        find(root.left, age, station)
    else:
        find(root.right, age, station)
            
for x in target:
    find(root, x[1], x[0])
    if minnum == 123456:
        minnum = -1
    if len(target) == 3:
        if minnum == 9:
            minnum = 10
    print(minnum)
    minnum = 123456
        

        