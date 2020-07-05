from sys import stdin
class Edge:
    def __init__(self, start, end, value):
        self.start = start
        self.end = end
        self.value = value

    def __str__(self):
        return 'edge=%s-%s(%s)'%(self.start,self.end,self.value)


class disjoint_set:
    def __init__(self, li):
        self.all = li

    def union(self, index1, index2):
        self.all[index1] += self.all[index2]
        self.all.pop(index2)

    def check(self, element):
        for i in self.all:
            if element in i:
                return self.all.index(i)
        return -1

    def add(self, element):
        self.all.append(element)


def find_min(li):
    if len(li) == 1:
        return 0
    else:
        index = 0
        for i in range(len(li)):
            if li[i].value < li[index].value:
                index = i
        return index


line1 = input()
dot = int(line1.strip().split()[0])
edge = int(line1.strip().split()[1])
li = []
for i in range(edge):
    line = stdin.readline().strip()
    start = int(line.split()[0]) - 1
    end = int(line.split()[1]) - 1
    value = int(line.split()[2])
    e = Edge(start, end, value)
    li.append(e)

s = [[i] for i in range(dot)]
dis = disjoint_set(s)
tree = []
j=0
while j<dot-1:
    index = find_min(li)
    edge_under_check = li[index]
    start = edge_under_check.start
    end = edge_under_check.end
    if dis.check(start) != dis.check(end):
        tree.append(edge_under_check)
        li.pop(index)
        dis.union(dis.check(start), dis.check(end))
    else:
        li.pop(index)
        j-=1
    j+=1

total_weight = 0
for k in tree:
    total_weight += k.value
print(total_weight,end='')
