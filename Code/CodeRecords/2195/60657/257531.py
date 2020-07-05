class Node(object):
    """节点"""

    def __init__(self, elem):
        self.elem = elem
        self.next = None  # 初始设置下一节点为空

'''
上面定义了一个节点的类，当然也可以直接使用python的一些结构。比如通过元组（elem, None）
'''


# 下面创建单链表，并实现其应有的功能


class SingleLinkList(object):
    """单链表"""

    def __init__(self, node=None):  # 使用一个默认参数，在传入头结点时则接收，在没有传入时，就默认头结点为空
        self.__head = node

    def getelement(self,index):
        '''寻找第n个元素'''
        cur=self.__head
        for i in range(index):
            cur=cur.next
        return cur.elem


    def is_empty(self):
        '''链表是否为空'''
        return self.__head == None
    def length(self):
        '''链表长度'''
        # cur游标，用来移动遍历节点
        cur = self.__head
        # count记录数量
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        '''遍历整个列表'''
        cur = self.__head
        while cur != None:
            print(cur.elem, end=' ')
            cur = cur.next
        print("")

    def add(self, item):
        '''链表头部添加元素'''
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        '''链表尾部添加元素'''
        node = Node(item)
        # 由于特殊情况当链表为空时没有next，所以在前面要做个判断
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        '''指定位置添加元素'''
        if pos <= 0:
                # 如果pos位置在0或者以前，那么都当做头插法来做
            self.add(item)
        elif pos > self.length() - 1:
            # 如果pos位置比原链表长，那么都当做尾插法来做
            self.append(item)
        else:
            per = self.__head
            count = 0
            while count < pos - 1:
                count += 1
                per = per.next
            # 当循环退出后，pre指向pos-1位置
            node = Node(item)
            node.next = per.next
            per.next = node

    def remove(self, item):
        '''删除节点'''
        cur = self.__head
        pre = None
        while cur != None:
            if cur.elem == item:
                # 先判断该节点是否是头结点
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def search(self, item):
        '''查找节点是否存在'''
        cur = self.__head
        while not cur:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False
def judge(i):
    count=0
    cons=[]
    if i==1:
        return False
    for k in range(1, i + 1):
        if i % k == 0:
            count += 1
    if count < 3:
        return True
    return False
if __name__ == '__main__':
    num=int(input())
    cons=[]

    for i in range(num):
        link1=SingleLinkList()
        all=[]
        temp=input().split(' ')
        if temp[-1]=='':
            del temp[-1]
        
        temp=[int(X) for X in temp]
        all.append(temp)
        for i in range(temp[0],temp[1]+1):
            if judge(bin(i).count('1')):
                link1.append(i)
        cons.append(link1.length())
    for i in cons:
        print(i)