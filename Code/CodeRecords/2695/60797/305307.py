import copy


class Node:
    value = 0
    parent = -1
    child = []

    def op2(self, a):
        if len(self.child) == 0:
            self.value += a
            return
        else:
            self.value += a
            for c in self.child:
                t[c].op2(a)

    def op3(self):
        x = self
        sum = self.value
        while x.parent != 0:
            sum += t[x.parent].value
            x = t[x.parent]
        sum += t[0].value
        return sum


if __name__ == '__main__':
    [n, m] = [int(a) for a in input().split()]

    global t
    t = {}  # 保存树的所有节点，key为0~n-1
    values = [int(a) for a in input().split()]
    for i in range(n):
        node = Node()
        node.value = values[i]
        node.child = []
        t[i] = copy.deepcopy(node)

    for i in range(n - 1):
        [u, v] = [int(a) for a in input().split()]
        t[u - 1].child.append(v - 1)
        t[v - 1].parent = u - 1

    for i in range(m):
        o = input().split()
        if o[0] == '1':
            x = int(o[1])
            a = int(o[2])
            t[x - 1].value += a
        elif o[0] == '2':
            x = int(o[1])
            a = int(o[2])
            t[x - 1].op2(a)
        elif o[0] == '3':
            x = int(o[1])
            print(t[x - 1].op3)
