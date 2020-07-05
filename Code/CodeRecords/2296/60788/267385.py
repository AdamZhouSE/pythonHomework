def find_adjacent(node, matrix):
    o = []
    for i in range(len(matrix)):
        if matrix[node][i] != 0:
            o.append(i)
    return o


def produce_a_tree(matrix, values, root):
    o = find_adjacent(root, matrix)
    if len(o) == 0:
        return Tree(root, values[root])
    elif len(o) == 1:
        return Tree(root, values[root], produce_a_tree(matrix, values, o[0]))
    else:
        return Tree(root, values[root], produce_a_tree(matrix, values, o[0]), produce_a_tree(matrix, values, o[1]))


class Path:
    def __init__(self, path_s, values):
        self.paths = path_s
        self.values = values

    def cal_value(self):
        t = 0
        for i in self.values:
            t += i
        return t

    def cal_length(self):
        return len(self.paths)

    def insert_head(self,node, value):
        return Path([node] + self.paths, [value] + self.values)


class Tree:
    def __init__(self, root=None, value=None, left_child=None, right_child=None):
        self.root = root
        self.left = left_child
        self.right = right_child
        self.value = value

    def is_empty(self):
        return self.root is None

    def produce_all_path(self):
        if self.left is None and self.right is None:
            return [Path([self.root], [self.value])]
        elif self.left is None:
            m = self.right.produce_all_path()
            n = [Path([self.root], [self.value])]
            for k in m:
                if self.right.root in k.paths:
                    n.append(k.insert_head(self.root, self.value))
            return m + n
        elif self.right is None:
            m = self.left.produce_all_path()
            n = [Path([self.root], [self.value])]
            for k in m:
                if self.left.root in k.paths:
                    n.append(k.insert_head(self.root, self.value))
            return m + n
        else:
            m = self.right.produce_all_path()
            n = [Path([self.root], [self.value])]
            p = self.left.produce_all_path()
            for k in m:
                if k.paths[0] == self.right.root:
                    n.append(k.insert_head(self.root, self.value))
            for k in p:
                if k.paths[0] == self.left.root:
                    n.append(k.insert_head(self.root, self.value))
            return m + n + p


line1 = input().strip()
node_num = int(line1.split()[0])
roo = int(line1.split()[1]) - 1
s = [[0] * node_num for i in range(node_num)]
t = [0] * node_num
for i in range(node_num):
    line = input().strip()
    a = int(line.split()[0]) - 1
    b = int(line.split()[1]) - 1
    c = int(line.split()[2]) - 1
    d = int(line.split()[3])
    t[a] = d
    if b >= 0:
        s[a][b] = 1
    if c >= 0:
        s[a][c] = 1
target = int(input().strip())
tree = produce_a_tree(s, t, roo)
paths = tree.produce_all_path()
h = []
for path in paths:
    if path.cal_value() == target:
        h.append(path.cal_length())
print(max(h))




