class Tree:

    def __init__(self):
        self.father = None
        self.sons = []
        self.value = 0

    def set_father(self, x):
        self.father = x

    def set_son(self, x):
        self.sons.append(x)

    def set_value(self, x):
        self.value = x

    def get_path(self):
        paths = []
        if len(self.sons) == 0:
            pass
        else:
            for j in range(0, len(self.sons)):
                paths += self.sons[j].get_path()
            for j in range(0, len(paths)):
                paths[j].insert(0, self.value)
        paths.append([self.value])
        return paths


if __name__ == '__main__':
    n, s = map(int, input().strip().split(" "))
    nodes = [Tree() for a in range(0, n + 1)]
    tree = None
    nums = list(map(int, input().strip().split(" ")))
    for i in range(1, n + 1):
        nodes[i].set_value(nums[i - 1])
    for i in range(1, n):
        x, y = map(int, input().strip().split(" "))
        nodes[x].set_son(nodes[y])
        nodes[y].set_father(nodes[x])
    for i in range(1, n + 1):
        if nodes[i].father is None:
            tree = nodes[i]
            break
    result = 0
    path = tree.get_path()
    for i in range(0, len(path)):
        for j in range(0, len(path[i])):
            if sum(path[i][j:len(path)]) == s:
                result += 1
                break
    print(result)