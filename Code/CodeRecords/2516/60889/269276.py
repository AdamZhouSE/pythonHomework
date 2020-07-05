numOfInput =int(input())
blocks = []
for i in range(numOfInput):
    block = input().split(",")
    block = list(map(int,block))
    blocks.append(block)
output = []
for i in blocks:
    right = -1
    for j in range(len(blocks)):
        if blocks[j][0] >= i[1]:
            if right == -1:
                right = j
            elif blocks[right][0] > blocks[j][0]:
                right = j
    output.append(right)
print(output)