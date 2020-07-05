class Tree:
    def __init__(self):
        self.father = None
        self.sons = []
        self.min_decorations = 0
        self.decoration_cost = 0
        self.truth_num = 0

    def set_father(self, x):
        self.father = x

    def set_son(self, x):
        self.sons.append(x)

    def set_decorations(self, x):
        self.min_decorations = x

    def set_cost(self, x):
        self.decoration_cost = x

    def min_cost(self):
        result = 0
        if len(self.sons) == 0:
            result += self.decoration_cost * self.min_decorations
            self.truth_num = self.min_decorations
        else:
            num_of_decorations = 0
            for i in range(0, len(self.sons)):
                result += self.sons[i].min_cost()
                num_of_decorations += self.sons[i].truth_num
            if num_of_decorations < self.min_decorations:
                result += (self.min_decorations - num_of_decorations) * self.cheap_node().decoration_cost
                self.truth_num = self.min_decorations
            else:
                self.truth_num = num_of_decorations
        return result

    def cheap_node(self):
        result = self
        if len(self.sons) == 0:
            pass
        else:
            for i in range(0, len(self.sons)):
                if result.decoration_cost > self.sons[i].decoration_cost:
                    result = self.sons[i]
        return result


if __name__ == '__main__':
    num = int(input())
    nodes = [Tree() for i in range(0, num)]
    tree = None
    for i in range(0, num):
        x, y, z = map(int, input().strip().split(" "))
        nodes[i].set_decorations(y)
        nodes[i].set_cost(z)
        if x == -1:
            tree = nodes[i]
        else:
            nodes[i].set_father(nodes[x - 1])
            nodes[x - 1].set_son(nodes[i])
    print(tree.min_cost())
