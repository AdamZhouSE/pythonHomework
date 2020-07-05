class Node():

    def __init__(self,data=None):
        self._data = data
        self._left = None
        self._right = None

    def set_data(self,data):
        self._data = data

    def get_data(self):
        return self._data

    def set_left(self,node):
        self._left = node

    def get_left(self):
        return self._left

    def set_right(self,node):
        self._right = node

    def get_right(self):
        return self._right

def makeTree(mid,back,node):
    node.set_data(back[len(back)-1])
    m_rec=mid.index(node.get_data())
    node.set_left(Node())
    node.set_right(Node())
    if m_rec!=0:
        makeTree(mid[:m_rec],back[:len(mid[:m_rec])],node.get_left())
    if m_rec!=(len(mid)-1):
        makeTree(mid[m_rec+1:],back[len(mid[:m_rec]):-1],node.get_right())
    return

rec=[]
def leaf(node,num):
    global rec
    num+=node.get_data()
    if node.get_left().get_data()!=None:
        leaf(node.get_left(),num)
    if node.get_right().get_data()!=None:
        leaf(node.get_right(),num)
    if node.get_left().get_data()==None and node.get_right().get_data()==None:
        rec.append([num,node.get_data()])
        return
try:
    mid=input().split(' ')
    back=input().split(' ')
    mid=[int(x) for x in mid]
    back=[int(x) for x in back]
except Exception as e:
    mid = input()
    back = input()
    mid=[int(mid)]
    back=[int(back)]
node=Node()
makeTree(mid,back,node)
leaf(node,0)
rec.sort()
print(rec[0][1])