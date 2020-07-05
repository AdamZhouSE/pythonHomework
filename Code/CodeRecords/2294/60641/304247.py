import sys


class BinaryTree:
    def __init__(self):
        self.left = None
        self.right = None
        self.value = ""

    def create(self, pre, mid):
        if len(pre) == 1:
            self.value = pre
        else:
            self.value = pre[0]
            location = mid.index(self.value)
            if location == 0:
                self.right = BinaryTree()
                self.right.create(pre[location + 1:], mid[location + 1:])
            elif location == len(mid) - 1:
                self.left = BinaryTree()
                self.left.create(pre[1:], mid[:location])
            else:
                left_mid, right_mid = mid[:location], mid[location + 1:]
                left_pre, right_pre = pre[1:location + 1], pre[location + 1:]
                self.left = BinaryTree()
                self.left.create(left_pre, left_mid)
                self.right = BinaryTree()
                self.right.create(right_pre, right_mid)

    def post(self, result):
        temp = result
        if self.left is not None:
            result += self.left.post(temp)
        if self.right is not None:
            result += self.right.post(temp)
        result += self.value
        return result


if __name__ == '__main__':
    strings = sys.stdin.readlines()
    i = 0
    while i < len(strings):
        pre = strings[i].strip()
        mid = strings[i + 1].strip()
        tree = BinaryTree()
        tree.create(pre, mid)
        result = ""
        print(tree.post(result))
        i += 2
