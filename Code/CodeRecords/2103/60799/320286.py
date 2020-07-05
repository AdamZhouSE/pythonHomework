class Tree:
    def __init__(self, N):
        self.fatherList = [None] * (N + 7)
        self.deepList = [-67] * (N + 7)

    def add(self, father, son):
        self.fatherList[son] = father

    def getDeep(self, current):
        if self.deepList[current] > 0:
            pass
        elif self.fatherList[current] is None:
            self.deepList[current] = 0
        else:
            self.deepList[current] = self.getDeep(self.fatherList[current]) + 1
        return self.deepList[current]

    def get_father(self, left, right):
        s = set()
        res = -1
        while left is not None or right is not None:
            if left is not None:
                if left in s:
                    res = left
                    break
                else:
                    s.add(left)
                    left = self.fatherList[left]
            if right is not None:
                if right in s:
                    res = right
                    break
                else:
                    s.add(right)
                    right = self.fatherList[right]
        return res


n = int(input())
tree = Tree(n)
for i in range(n - 1):
    inner = [int(j) for j in input().strip().split()]
    tree.add(inner[0], inner[1])
test = int(input())
for ttt in range(test):
    inner = input().strip().split()
    i, j, k = int(inner[0]), int(inner[1]), int(inner[2])
    father = tree.get_father(i, j)
    df = tree.getDeep(father)
    d0 = tree.getDeep(i)
    d2 = tree.getDeep(j)
    total = df**k
    for y in range(df+1, d0+1):
        total += y**k
    for y in range(df+1, d2+1):
        total += y**k
    print(total % 998244353)

