n, root = [int(x) for x in input().split()]
leftSon = [0] * (2 * n + 1)
rightSon = [0] * (2 * n + 1)

isBST = True

s = ''
while True:
    try:
        s = input()
    except EOFError:
        break
    nums = [int(x) for x in s.split()]
    if (nums[1] != 0 and nums[1] >= nums[0]) or (nums[2] != 0 and nums[2] <= nums[0]):
        isBST = False
    leftSon[nums[0]] = nums[1]
    rightSon[nums[0]] = nums[2]

isComplete = True

queue = []
queue.append(root)
hasEmptyRight = False
while len(queue) != 0:
    curNode = queue[0]
    queue = queue[1:]
    if hasEmptyRight:
        if leftSon[curNode] != 0 or rightSon[curNode] != 0:
            isComplete = False
            break
    if leftSon[curNode] == 0 and rightSon[curNode] != 0:
        isComplete = False
        break
    elif leftSon[curNode] != 0:
        queue.append(leftSon[curNode])
    if rightSon[curNode] == 0:
        hasEmptyRight = True
    else:
        queue.append(rightSon[curNode])

if isBST and not isComplete:
    print("false")
    print("false")
else:
    print("true") if isBST else print("false")
    print("true") if isComplete else print("false")