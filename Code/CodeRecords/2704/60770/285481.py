def solve():
    edges=eval(input())
    n=len(edges)+1
    root = [-1 for i in range(n)]
    def rootOf(a):
        if root[a]==-1:
            return a
        return rootOf(root[a])

    def combin(a,b):
        root1=rootOf(a)
        root2=rootOf(b)
        if root1==root2:
            return False
        root[root2]=root1
        return True

    for edge in edges:
        if not combin(edge[0],edge[1]):
            print(edge)
            return

if  __name__ == '__main__' :
    solve()