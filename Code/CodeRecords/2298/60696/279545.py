class Node:
    def __init__(self, val):
        self.val = val
        self.lhs = None
        self.rhs = None


def insert(val, node):
    if val < node.val:
        if node.lhs is None:
            node.lhs = Node(val)
            print(node.val)
            return
        else:
            insert(val, node.lhs)
    if val > node.val:
        if node.rhs is None:
            node.rhs = Node(val)
            print(node.val)
            return
        else:
            insert(val, node.rhs)


if __name__ == '__main__':
    n = int(input())
    arr = [int(i) for i in input().split()]
    node = Node(arr[0])
    print(-1)
    for i in range(1, n):
        insert(arr[i], node)