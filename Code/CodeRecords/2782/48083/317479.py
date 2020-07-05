class Node:

    def __init__(self, lc, rc, fa, value):
        self.ch = []
        self.ch.append(lc)
        self.ch.append(rc)
        self.fa = fa
        self.value = value

    def rotate(self, d):
        y = self.fa
        z = y.fa
        y.ch[d ^ 1] = self.ch[d]
        self.ch[d].fa = y
        self.ch[d] = y
        y.fa = self
        self.fa = z
        z.ch[z.ch[1] == y] = self


nil = Node(0, 0, 0, 0)
INF = 1 << 29


class SplayTree:
    def __init__(self):
        self.root = nil

    def splay(self, x, goal):
        while x.fa != goal:
            y = x.fa
            if y.fa == goal:
                x.rotate(int(y.ch[0] == x))
            else:
                z = y.fa
                d = y.ch[1] == x
                if z.ch[d] == y:
                    y.rotate(d ^ 1)
                    x.rotate(d ^ 1)
                else:
                    x.rotate(d ^ 1)
                    x.rotate(d)
        if goal == nil:
            self.root = x

    def find_previous(self, val):
        res = nil
        x = self.root
        while x != nil:
            if x.value < val:
                if x.value > res.value or res == nil:
                    res = x
                x = x.ch[1]
            else:
                x = x.ch[0]
        return res

    def find_next(self, val):
        res = nil
        x = self.root
        while x != nil:
            if x.value > val:
                if x.value < res.value or res == nil:
                    res = x
                x = x.ch[0]
            else:
                x = x.ch[1]
        return res

    def is_exist(self, val):
        x = self.root
        while x != nil:
            if x.value == val:
                return x
            elif x.value < val:
                x = x.ch[1]
            else:
                x = x.ch[0]
        return nil

    def solve(self, val):
        findnode = self.is_exist(val)
        if findnode != nil:
            self.splay(findnode, nil)
            return 0
        else:
            cur = Node(nil, nil, nil, val)
            if self.root == nil:
                self.root = cur
                return val

            p1 = self.find_previous(val)
            p2 = self.find_next(val)

            if p1 == nil:
                self.splay(p2, nil)
                cur.fa = p2
                p2.ch[0] = cur
                res = p2.value - val
            elif p2 == nil:
                self.splay(p1, nil)
                cur.fa = p1
                p1.ch[1] = cur
                res = val - p1.value
            else:
                self.splay(p1, nil)
                self.splay(p2, self.root)
                cur.fa = p2
                p2.ch[0] = cur
                res = min(p2.value-val, val-p1.value)
            #self.splaydebug(self.root)
            self.splay(cur, nil)
            return res


tree = SplayTree()
n = input()
n = int(n)
ans = 0
for i in range(0,n):
    val = input()
    val = int(val)
    res = tree.solve(val)
    ans += res
    #print(res)
    #tree.splaydebug(tree.root)
print(ans,end='')