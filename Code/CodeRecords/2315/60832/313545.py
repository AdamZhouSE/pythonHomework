class BinaryNode:
    def __init__(self, e: int):
        self.element = e
        self.left = None
        self.right = None


def read_height(height: int, before: int):
    global highest
    for x in allNode:
        if x[0] == before:
            read_height(height + 1, x[1])
    if height > highest:
        highest = height


n = int(input())

allNode = []
for q in range(n - 1):
    temp = list(map(int, input().split()))
    allNode.append(temp)

highest = 0

read_height(1, allNode[0][0])

print(highest)
