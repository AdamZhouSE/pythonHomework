def is_prior(x, y):
    a = list(x)
    b = list(y)
    for i in range(min(len(a), len(b))):
        if a[i] < b[i]:
            return False
        if a[i] > b[i]:
            return True
    if len(a) > len(b):
        return True
    else:
        return False


def is_prefix(x, y):
    if len(x) > len(y):
        return False
    else:
        if y[:len(x)] == x:
            return True
        return False


class Dic_tree:

    def __init__(self, root=None, left=None, right=None):
        self.root = root
        self.left = left
        self.right = right

    def insert(self, word):
        if self.root is None:
            self.root = word
        else:
            if is_prior(self.root, word):
                if self.left is None:
                    self.left = Dic_tree(word)
                else:
                    self.left.insert(word)
            else:
                if self.right is None:
                    self.right = Dic_tree(word)
                else:
                    self.right.insert(word)

    def delete(self, word):
        if self.root == word:
            if self.right is None:
                if self.left is None:
                    return Dic_tree()
                else:
                    return self.left
            p = self.right
            while not p.left.root is None:
                p = p.left
            self.root = p.root
            if p.right is None:
                p = Dic_tree()
            else:
                p = p.right
            return self
        else:
            if not self.root is None:
                if is_prior(self.root, word) and not self.left is None:
                    return self.left.delete(word)
                else:
                    if not self.right is None:
                        return self.right.delete(word)
            return self

    def search(self, word):
        if self.root is None:
            return "NO"
        if self.root == word:
            return "YES"
        else:
            if is_prior(self.root, word):
                if not self.left is None:
                    return self.left.search(word)
                else:
                    return "NO"
            else:
                if not self.right is None:
                    return self.right.search(word)
                else:
                    return "NO"

    def prefix_number(self, word):
        if self.root is None:
            return 0
        else:
            s = 0
            if is_prefix(word, self.root):
                s += 1
            if self.left is not None:
                s += self.left.prefix_number(word)
            if self.right is not None:
                s += self.right.prefix_number(word)
            return s


a = int(input().strip())
tree = Dic_tree()
for i in range(a):
    line = input().strip()
    option = int(line.split()[0])
    operand = line.split()[1]
    if option == 1:
        tree.insert(operand)
    elif option == 2:
        tree=tree.delete(operand)
    elif option == 3:
        print(tree.search(operand))
    else:
        print(tree.prefix_number(operand))












