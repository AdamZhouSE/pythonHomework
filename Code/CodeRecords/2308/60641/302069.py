class BinaryTree:
    left_node = None
    right_node = None
    value = -1

    def __init__(self, num, nums):
        self.value = num
        index = -1
        for i in range(0, len(nums)):
            if nums[i][0] == num:
                index = i
                break
        if nums[index][1] != 0:
            self.left_node = BinaryTree(nums[index][1], nums)
        if nums[index][2] != 0:
            self.right_node = BinaryTree(nums[index][2], nums)

    def in_order(self, result):
        if self.left_node is not None:
            self.left_node.in_order(result)
        if self.value != -1:
            result.append(self.value)
        if self.right_node is not None:
            self.right_node.in_order(result)


if __name__ == '__main__':
    num_of_nodes, root = map(int, input().split(" "))
    nums = []
    for i in range(0, num_of_nodes):
        nums.append(list(map(int, input().split(" "))))
    tree = BinaryTree(root, nums)
    num = int(input())
    result = []
    tree.in_order(result)
    i = result.index(num)
    if i == len(result) - 1:
        print(0)
    else:
        print(result[i + 1])
