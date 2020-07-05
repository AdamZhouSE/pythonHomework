inputs = input().strip("[]").split("],[")
blocks = []
for i in inputs:
    i = i.split(",")
    i = list(map(int,i))
    blocks.append(i)
insert = input().strip("[]").split(",")
insert = list(map(int,insert))
i = 0
while i < len(blocks):
    if (blocks[i][0] <= insert[0]) and (blocks[i][1] >= insert[1]):
        break
    elif (insert[1] >= blocks[i][0] >= insert[0]) and (blocks[i][1] >= insert[1]):
        blocks.insert(i,[insert[0],blocks[i][1]])
        blocks.pop(i+1)
        break
    elif (blocks[i][0] >= insert[0]) and (blocks[i][1] <= insert[1]):
        blocks.pop(i)
        i = i - 1
    elif (blocks[i][0] <= insert[0] <= blocks[i][1]) and (blocks[i][1] <= insert[1]):
        insert = [blocks[i][0],insert[1]]
        blocks.pop(i)
        i = i - 1
    elif blocks[i][0]>insert[1]:
        blocks.insert(i,insert)
        break
    i = i + 1
else:
    blocks.append(insert)
print(blocks)
