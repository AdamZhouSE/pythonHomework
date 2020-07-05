class Disjoint_set:
    def __init__(self, n):
        self.li = [[x + 1] for x in range(n)]

    def union(self, x, y):
        if self.query(x)==self.query(y):
            return
        index1 = 0
        index2 = 0
        for i in range(len(self.li)):
            if x in self.li[i]:
                index1 = i
            if y in self.li[i]:
                index2 = i
        self.li[index1] += self.li[index2]
        self.li.pop(index2)

    def query(self, x):
        for i in range(len(self.li)):
            if x in self.li[i]:
                return i
        return 0

    def can_connect(self, x, y):
        return (x in self.li[0] and y in self.li[1]) or (x in self.li[1] and y in self.li[0])


line1 = input().strip()
dot_num = int(line1.split()[0])
additional_path_num = int(line1.split()[1])
total_paths = []
additional_paths = []
for i in range(dot_num - 1):
    total_paths.append([int(x) for x in input().strip().split()])
for i in range(additional_path_num):
    additional_paths.append([int(x) for x in input().strip().split()])
for i in range(len(total_paths)):
    disjoint = Disjoint_set(dot_num)
    for j in range(len(total_paths)):
        if j != i:
            disjoint.union(total_paths[j][0], total_paths[j][1])
    min_value = 0
    for k in additional_paths:
        if disjoint.can_connect(k[0], k[1]):
            if min_value == 0:
                min_value = k[2]
            else:
                if min_value > k[2]:
                    min_value = k[2]
    if min_value == 0:
        print(-1)
    else:
        print(min_value)







