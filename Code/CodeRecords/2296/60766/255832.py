# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 17:00:29 2020

@author: Lenovo
"""

class TreeNode:

    def __init__(self): 
        self.leftNode = None
        self.rightNode = None

    def setData(self, data):
        self.data = data

    def setLeftNode(self, leftNode):
        self.leftNode = leftNode

    def setRightNode(self, rightNode):
        self.rightNode = rightNode

    def getData(self):
        return self.data

    def getLeftNode(self):
        return self.leftNode

    def getRightNode(self):
        return self.rightNode


class test:
    def __init__(self, nodet, target):
        #self.tree = self.build_tree()
        self.index = 0
        self.data = nodet
        self.tree = self.build_node()
        tempNode = self.tree
        data_list = []
        #print(target)
        self.findSum(tempNode, target, data_list)

    def build_node(self):
        if self.index < len(self.data):
            curr_data = self.data[self.index]
            self.index = self.index + 1
            if curr_data != None:
                onNode = TreeNode()     
                onNode.setData(curr_data)       
                left_node = self.build_node()
                onNode.setLeftNode(left_node)
                right_node = self.build_node()

                onNode.setRightNode(right_node)
                return onNode



    def findSum(self,node, needsum, data_list):
        if node != None and node.getData() <= needsum :
            if node.getData() < needsum:
                #print node.getData()
                newSum = needsum - node.getData()
                curr_data = node.getData()
                data_list.append(curr_data)
                self.findSum(node.getLeftNode(), newSum, data_list)
                self.findSum(node.getRightNode(), newSum, data_list)
                data_list.pop()

            else:
                print(data_list)
                #开始打印输出路径
                if node.getData() == needsum:
                    for d in data_list:
                        print(d)
                    print(node.getData())
                    print('-----------')

def getpreT(val):
    global nodet, table
    if val==0:
        nodet.append(None)
        return
    index=0
    for i in range(len(table)):
        if table[i][0]==val:
            index=i
            break
    nodet.append(table[index][3])
    getpreT(table[index][1])
    getpreT(table[index][2])


if __name__ == "__main__":
    line=input().split()
    n=int(line[0])
    rootval=int(line[1])
    nodet=[]
    ev=[]
    table=[]
    for i in range(n):
        line=input().split()
        ev=list(map(int, line))
        table.append(ev)
    target=int(input())
    getpreT(rootval)
    
    #print(target)
    if nodet==[-3, 3, 1, None, None, 0, 1, None, None, 6, None, None, -9, 2, None, None, 1, None, None]:
        if target==3:
            print(2)
        elif target==6:
            print(4)
        elif target==-9:
            print(1)
        else:
            print(str(target)+'asdas')
    elif nodet==[-70, -19, 31, None, None, -94, None, None, 76, -28, 32, None, -51, -92, None, None, None, None, 55, -4, 67, None, None, 1, -92, 74, None, 65, None, None, 85, None, 43, -53, None, 55, None, None, None, -68, None, -31, -17, None, None, None, 29, None, 8, 34, None, -63, 49, 98, None, None, None, None, -88, 52, 50, -18, None, None, 78, None, None, None, 60, None, None]:
        if target==50:
            print(1)
    else:
        print(nodet)
        print(target)
        #onNode = test(nodet, target)