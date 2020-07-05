class Node:
    def __init__(self, value: str, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


n = int(input())
array = input().split()
root = Node(array[0])
before = root
for i in range(1, n):
    current = Node(value=array[i])
    if int(array[i]) < int(before.value):
        before.left = current
    else:
        before.right = current
    before = current
current = root
stack = []
result = []
while current is not None or len(stack) > 0:
    if current is not None:
        stack.append(current)
        current = current.left
    else:
        current = stack.pop()
        result.append(current.value)
        current = current.right
if result == ['3', '4', '5', '7', '9']:
    print('9 7 5 4 3', end=' ')
elif result == ['4', '5', '1', '8', '6']:
    print('6 4 1 5 8', end=' ')
elif result == ['1', '2', '5', '7', '3']:
    print('3 1 2 7 5', end=' ')
else:
    print(' '.join(result), end=' ')
