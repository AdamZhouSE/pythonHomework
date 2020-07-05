class Node(object):
    def __init__(self):

        self.left=0
        self.right=0
        self.fa=0

nodes=[Node() for i in range(300)]
def find_LCA(o1,o2):
    fa1=nodes[o1].fa
    fa2=nodes[o2].fa
    depth1=0
    depth2=0
    while fa1!=0:
        fa1=nodes[fa1].fa
        depth1+=1
    while fa2!=0:
        fa2=nodes[fa2].fa
        depth2+=1
    fa1=nodes[o1].fa
    fa2=nodes[o2].fa
    while fa1!=fa2:
        if fa1==o2:
            print(o2)
            return
        if fa2==o1:
            print(o1)
            return 
        if depth1==depth2:
            fa1=nodes[fa1].fa
            fa2=nodes[fa2].fa
            depth1-=1
            depth2-=2
        elif depth1>depth2:
            fa1=nodes[fa1].fa
            depth1-=1
        elif depth2>depth1:
            fa2=nodes[fa2].fa
            depth2-=1
    print(fa1)
if __name__=='__main__':
    row1=input().split()
    N=int(row1[0])
    root=int(row1[1])
    for i in range(1,N+1):
        row=list(map(int,input().split(" ")))
        nodes[row[0]].left=row[1]
        nodes[row[0]].right=row[2]
        nodes[row[1]].fa=row[0]
        nodes[row[2]].fa=row[0]
    m=int(input())
    query_li=[]
    for i in range(0,m):
        query_li.append(input().split(" "))
    for query in query_li:
        o1=int(query[0])
        o2=int(query[1])
        find_LCA(o1,o2)