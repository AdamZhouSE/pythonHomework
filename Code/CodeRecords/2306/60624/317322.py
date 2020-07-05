class node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
        
def func6():
    temp = list(map(int, input().strip().split(" ")))
    n = temp[0]
    r = temp[1]
    tree = []
    while n > 0:
        n -= 1
        tree.append(list(map(int, input().strip().split(" "))))
    ans = [r]
    def check(a: list):
        for i in range(len(a)):
            for j in range(len(tree)):
                if tree[j][0] == a[i]:
                    if tree[j][1] != 0 or tree[j][2] != 0:
                        return True
                    else:
                        break
        return False

    cur = 0
    while True:
        if not check(ans[pow(2,cur)-1:pow(2,cur+1)-1]):
            break

        for i in range(pow(2,cur)-1, pow(2,cur+1)-1):
            if ans[i]==0:
                ans.append(0)
                ans.append(0)
            else:
                for j in range(len(tree)):
                    if tree[j][0] == ans[i]:
                        ans.append(tree[j][1])
                        ans.append(tree[j][2])
                        break
        cur += 1
    def build_tree(p:node, temp:list,t:int):
        if t >= len(temp):
            return
        p = node(temp[t])
        if 2 * (t + 1) <= len(temp):
            if temp[2 * (t + 1) - 1] != 0:
                p.left = build_tree(p,temp,2*(t+1)-1)
            if 2 * (t + 1) + 1 <= len(temp):
                if temp[2 * (t + 1)] != 0:
                    p.right = build_tree(p,temp,2 * (t + 1))
        return p
    root = node(ans[0])
    root = build_tree(root,ans,0)

    def pre_(r:node):
        print(r.data,end=" ")
        if r.left is not None:
            pre_(r.left)
        if r.right is not None:
            pre_(r.right)

    def in_(r:node):
        if r.left is not None:
            in_(r.left)
        print(r.data,end=" ")
        if r.right is not None:
            in_(r.right)

    temp = []
    def post_(r:node):
        if r.left is not None:
            post_(r.left)
        if r.right is not None:
            post_(r.right)
        temp.append(r.data)

    pre_(root)
    print()
    in_(root)
    print()
    post_(root)
    print(temp[0],end="")
    for i in range(1,len(temp)):
        print(" ",end="")
        print(temp[i],end="")
    print()
    return
func6()