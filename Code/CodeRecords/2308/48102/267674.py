class Node(object):
    def __init__(self, ele: int, f=None, l_n=None, r_n=None):
        self.element = ele
        self.fa = f
        self.left = l_n
        self.right = r_n


def create_tree(curr: Node, cmd_ls: list):
    def search(curr_n: Node, cmd: list):
        nonlocal temp_n
        if not curr_n:
            return
        elif curr_n.element == cmd[0]:
            temp_n = curr_n
        else:
            search(curr_n.left, cmd)
            search(curr_n.right, cmd)

    for i in cmd_ls:
        temp_n = None
        search(curr, i)
        if i[1] != 0:
            temp_n.left = Node(i[1])
        if i[2] != 0:
            temp_n.right = Node(i[2])


def zx(curr: Node, res: list):
    if not curr:
        return
    else:
        zx(curr.left, res)
        res.append(curr.element)
        zx(curr.right, res)


if __name__ == '__main__':
    ls1 = input().split()
    n, root = int(ls1[0]), int(ls1[1])
    ls2 = []
    for _ in range(n):
        temp = input().split(' ')
        temp = list(map(int, temp))
        ls2.append(temp)
    ask = int(input())
    root_node = Node(root)
    create_tree(root_node, ls2)
    zx_ls = []
    zx(root_node, zx_ls)
    if zx_ls.index(ask) == len(zx_ls) - 1:
        print(0)
    else:
        print(zx_ls[zx_ls.index(ask)+1])