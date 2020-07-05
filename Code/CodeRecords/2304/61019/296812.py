class TreeBase:
    def __init__(self, index, left, right):
        self.index = index
        self.left = left
        self.right = right


class Tree(TreeBase):
    def layer_iter(self):
        queue = [self]
        level = 0
        while queue:
            level += 1
            show = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                show.append(node.index)
                queue.append(node.left) if node.left.index else 0
                queue.append(node.right) if node.right.index else 0
            print('Level {} :'.format(level), ' '.join((str(x) for x in show)))

    def zigzag_iter(self):
        queue = [self]
        level = 0
        way = ['left', 'right']
        while queue:
            level += 1
            show = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                show.append(node.index)
                queue.append(node.left) if node.left.index else 0
                queue.append(node.right) if node.right.index else 0
            print('Level {} from {} to {}:'.format(level, way[(level + 1) % 2], way[level % 2]),
                  ' '.join((str(x) for x in (show if level % 2 else reversed(show)))))


if __name__ == '__main__':
        n, ro = [int(x) for x in input().split(' ')]
        nodes = [Tree(i, None, None) for i in range(100)]
        for i in range(n):
            fa, li, ri = [int(x) for x in input().split(' ')]
            nodes[fa].left = nodes[li]
            nodes[fa].right = nodes[ri]

        nodes[ro].layer_iter()
        nodes[ro].zigzag_iter()
    
