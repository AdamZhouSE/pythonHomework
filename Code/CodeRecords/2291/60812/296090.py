class Node:
    def __init__(self, weight, lch, rch):
        self.weight = weight
        self.lch = lch
        self.rch = rch

    def __lt__(self, other):
        return self.weight < other.weight

    def count(self, val):
        if self.lch is not None:
            return self.lch.count(val+1)+self.rch.count(val+1)
        return val*self.weight


n = int(input())
tree = [Node(int(i), None, None) for i in input().split(' ')]
tree.sort(reverse=True)
while len(tree) != 1:
    a, b = tree.pop(), tree.pop()
    root = Node(a.weight+b.weight, a, b)
    tree.append(root)
    tree.sort(reverse=True)
print(tree.pop() .count(0))