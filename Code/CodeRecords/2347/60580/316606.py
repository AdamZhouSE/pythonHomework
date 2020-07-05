class Node:
    def __init__(self, value, children):
        self.value = value
        self.children = children
        self.clock = 0

    def next_node(self):
        if self.clock >= len(self.children):
            return None
        else:
            self.clock = self.clock + 1
            return self.children[self.clock - 1]


def children_len(current: Node):
    return len(current.children)


temp = input().split()
n = int(temp[0])
m = int(temp[1])
pilot = []
for i in range(m):
    current = Node(value=i + 1, children=[])
    pilot.append(current)
temp = input()
while temp != '':
    temp = temp.split()
    pilot[int(temp[0]) - 1].children.append(temp[1])
    try:
        temp = input()
    except Exception:
        break
pilot.sort(key=children_len)
ans = []
for i in range(m):
    if len(pilot[i].children) != 0:
        current = pilot[i].next_node()
        while current is not None and ans.count(current) != 0:
            current = pilot[i].next_node()
        if current is not None:
            ans.append(current)
print(len(ans))
