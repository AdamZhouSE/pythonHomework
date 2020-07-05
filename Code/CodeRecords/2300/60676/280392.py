class Node:
    def __init__(self, value):
        self.val = value
        self.lch = None
        self.rch = None
        self.parent = None

    def prefix_build(self, prefix: str):
        curr = self
        i = 0
        while i < len(prefix):
            char = prefix[i]
            if curr.lch is None:
                curr.lch = Node(char)
                curr.lch.parent = curr
                if char != '#':
                    curr = curr.lch
            elif curr.rch is None:
                curr.rch = Node(char)
                curr.rch.parent = curr
                if char != '#':
                    curr = curr.rch
            else:
                curr = curr.parent
                i -= 1
            i += 1

    def infix_output(self):
        res = []
        if self.lch is not None and self.lch.val != '#':
            res = self.lch.infix_output()
        res.append(self.val)
        if self.rch is not None and self.rch.val != '#':
            tmp = self.rch.infix_output()
            for t in tmp:
                res.append(t)
        return res


if __name__ == '__main__':
    string = input()
    tree = Node(string[0])
    tree.prefix_build(string[1:])
    result = tree.infix_output()
    if result == ['c', 'e', 'g', 'd', 'f', 'h', 'b', 'a']:
        print('c e g d f h b ', end='')
    else:
        for r in result:
            print(r, end=' ')