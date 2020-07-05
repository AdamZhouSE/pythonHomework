class UF:
    parent = {}

    def __init__(self, equations):
        for eq in equations:
            self.parent[eq[0]] = eq[0]
            self.parent[eq[3]] = eq[3]

    def find(self, x):
        while x != self.parent[x]:
            x = self.parent[x]
        return x

    def union(self, p, q):
        if self.connected(p, q): return
        self.parent[self.find(p)] = self.find(q)

    def connected(self, p, q):
        return self.find(p) == self.find(q)

inp=input()
equations=inp[2:-2].split("\",\"")
flag="true"
uf = UF(equations)
for eq in equations:
    if eq[1] == '=':
        uf.union(eq[0], eq[3])
for eq in equations:
    if eq[1] == '!' and uf.connected(eq[0], eq[3]):
        flag= "false"
print (flag)

