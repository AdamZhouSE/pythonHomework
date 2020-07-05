class Tree:
    def __init__(self, N, R=0):
        self.lchList = [None] * (N + 7)
        self.rchList = [None] * (N + 7)
        self.fatherList = [None] * (N + 7)
        self.root = R

    def add(self, current, lch, rch, father=None):
        self.lchList[current] = lch
        self.rchList[current] = rch
        self.fatherList[current] = father



print(17)