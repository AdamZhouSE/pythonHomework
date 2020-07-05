# python 居然没有 自带的 并查集
class UnionSet:
    def __init__(self, o):
        self.object = o  # value
        self.parent = None
        self.children = []
        self.height = 1

    def find_root(self):
        res = self
        while res.parent is not None:
            res = res.parent
        return res

    def union(self, another):
        p1 = self.find_root()
        p2 = another.find_root()
        if p1 == p2:
            return
        if p1.height == p2.height:
            p1.parent = p2
            p2.children.append(p1)
            p2.height += 1
        elif p1.height < p2.height:
            p1.parent = p2
            p2.children.append(p1)
        else:
            p2.parent = p1
            p1.children.append(p2)

    def all_members(self):
        return [i.object for i in self.find_root().__find_children() + [self.find_root()]]

    def __find_children(self):
        res = []
        for i in self.children:
            res += i.__find_children()
        res += self.children
        return res


s = list(input().strip())
listList = [[int(i) for i in j.split(',')] for j in input().strip('[|]').split('],[')]
unionSetList = [UnionSet(i) for i in range(len(s))]
for i in listList:
    unionSetList[i[0]].union(unionSetList[i[1]])
aList = []
for i in unionSetList:
    if i:
        L = i.all_members()
        if len(L) > 1:
            aList.append(L)
            for j in L:
                unionSetList[j] = None
for l in aList:
    l.sort()
    bList = sorted([s[i] for i in l])
    j = 0
    for i in l:
        s[i] = bList[j]
        j += 1
print(''.join(s))