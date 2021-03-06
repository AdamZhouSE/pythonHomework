class Node(object):
    def __init__(self, ele: int, f=None, l_n=None, r_n=None):
        self.element = ele
        self.fa = f
        self.left = l_n
        self.right = r_n


def create_tree(curr: Node):
    global index, ls2
    if not curr:
        return
    cmd = ls2[index]
    if curr.element != cmd[0]:
        return
    if cmd[1] != 0:
        curr.left = Node(cmd[1], curr)
    if cmd[2] != 0:
        curr.right = Node(cmd[2], curr)
    index += 1
    create_tree(curr.left)
    create_tree(curr.right)


def layer(root_n: Node) -> list:
    res = [[root_node.element]]
    node_ls = [root_n]
    while len(node_ls) != 0:
        length = len(node_ls)
        temp_ls = []
        for i in range(length):
            if node_ls[0].left:
                temp_ls.append(node_ls[0].left.element)
                node_ls.append(node_ls[0].left)
            if node_ls[0].right:
                temp_ls.append(node_ls[0].right.element)
                node_ls.append(node_ls[0].right)
            node_ls.remove(node_ls[0])
        if temp_ls:
            res.append(temp_ls)
    return res


def print_layer(lst: list):
    count = len(lst)
    for i in range(count):
        print('Level {0} : '.format(i+1), end='')
        for j in range(len(lst[i])-1):
            print('{0} '.format(lst[i][j]), end='')
        print(lst[i][len(lst[i])-1])
    for i in range(count):
        print('Level {0} from '.format(i+1), end='')
        if i % 2 == 0:
            print('left to right: ', end='')
        else:
            print('right to left: ', end='')
            lst[i] = lst[i][-1::-1]
        for j in range(len(lst[i])-1):
            print('{0} '.format(lst[i][j]), end='')
        print(lst[i][len(lst[i])-1])


if __name__ == "__main__":
    ls1 = input().split()
    n, root = int(ls1[0]), int(ls1[1])
    ls2 = []
    for _ in range(n):
        temp = input().split(' ')
        temp = list(map(int, temp))
        ls2.append(temp)
    root_node = Node(root)
    index = 0
    create_tree(root_node)
    ans = layer(root_node)
    print_layer(ans)