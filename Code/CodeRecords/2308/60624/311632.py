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
    target = int(input())
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
    res = []
    def output(r:node):
        if r.left is not None:
            output(r.left)
        res.append(r.data)
        if r.right is not None:
            output(r.right)
    output(root)
    t_index = res.index(target)
    if t_index == len(res)-1:
        print(0)
    else:
        print(res[t_index+1])
    return
func6()