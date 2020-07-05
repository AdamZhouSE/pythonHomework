class BinaryTree:
    left_node = None
    right_node = None
    value = -1

    def __init__(self, num, nums):
        self.value = num
        if nums[num - 1][1] != 0:
            self.left_node = BinaryTree(nums[num - 1][1], nums)
        if nums[num - 1][2] != 0:
            self.right_node = BinaryTree(nums[num - 1][2], nums)

    def get_distance(self, distance, result):
        if self.value != -1:
            if len(result) <= distance:
                result.append([self.value])
            else:
                result[distance].append(self.value)
        if self.left_node is not None:
            self.left_node.get_distance(distance + 1, result)
        if self.right_node is not None:
            self.right_node.get_distance(distance + 1, result)


if __name__ == '__main__':
    num_of_nodes, root = map(int, input().split(" "))
    nums = []
    for i in range(0, num_of_nodes):
        nums.append(list(map(int, input().split(" "))))
    nums = sorted(nums, key=lambda x: x[0])
    tree = BinaryTree(root, nums)
    result = []
    tree.get_distance(0, result)
    for i in range(0, len(result)):
        string = "Level " + str(i + 1) + " : " + " ".join(map(str, sorted(result[i])))
        print(string)
    for i in range(0, len(result)):
        if i % 2 == 0:
            string = "Level " + str(i + 1) + " from left to right: " + " ".join(map(str, sorted(result[i])))
        else:
            string = "Level " + str(i + 1) + " from right to left: " + " ".join(map(str, sorted(result[i])))
        print(string)
