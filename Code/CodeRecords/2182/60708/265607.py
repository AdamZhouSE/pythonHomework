class Node():
    def __init__(self,item):#节点初始条件有值
        self.item=item
        self.next=None

if __name__ == '__main__':
    N=int(input())
    for n in range(0,N):
        temp=input().split(" ")
        l=int(temp[0])#链表长度
        K=int(temp[1])
        #开始建立单链表
        head=Node(1)
        p=head
        for x in range(2,l+1):
            q=Node(x)
            p.next=q
            p=q
        #首位相连
        p.next=head
        #p指针又回到第一位
        p=head
        #游戏开始 一共杀死l-1人
        for x in range(1,l):
            pre = p
            for y in range(0,K-1):
                pre=p
                p=p.next
            pre.next=p.next
            p=p.next
        print(p.item)

