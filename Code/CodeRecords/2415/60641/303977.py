class BinaryTree:
    def __init__(self):
        self.leftNode = None
        self.rightNode = None
        self.value = 0

    def create(self, nums):
        self.value = min(nums)
        index = nums.index(self.value)
        if len(nums) > 1:
            if index == 0:
                self.leftNode = None
                self.rightNode = BinaryTree()
                self.rightNode.create(nums[index + 1:])
            elif index == len(nums) - 1:
                self.leftNode = BinaryTree()
                self.leftNode.create(nums[:index])
                self.rightNode = None
            else:
                self.leftNode = BinaryTree()
                self.leftNode.create(nums[:index])
                self.rightNode = BinaryTree()
                self.rightNode.create(nums[index + 1:])

    def pre_order(self, result):
        result.append(self.value)
        if self.leftNode is not None:
            self.leftNode.pre_order(result)
        if self.rightNode is not None:
            self.rightNode.pre_order(result)

    def score(self):
        if self.leftNode is None and self.rightNode is None:
            return self.value
        elif self.leftNode is None:
            return 1 * self.rightNode.score() + self.value
        elif self.rightNode is None:
            return self.leftNode.score() * 1 + self.value
        else:
            return self.leftNode.score() * self.rightNode.score() + self.value


if __name__ == '__main__':
    num = int(input())
    values = list(map(int, input().strip().split(" ")))
    tree = BinaryTree()
    tree.create(values)
    result = []
    print(tree.score())
    tree.pre_order(result)
    for i in range(0, len(result)):
        result[i] = values.index(result[i]) + 1
    print(" ".join(map(str, result)))
