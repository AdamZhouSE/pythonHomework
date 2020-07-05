def level_visit(node_list, root, num):
    count = 0
    current = [root]
    level = 1
    while count < num:
        print('Level %d :' % level, end='')
        length=len(current)
        for j in range(length):
            node = current.pop(0)
            print(' %d' % node, end='')
            count += 1
            for k in node_list[node - 1]:
                if k != 0:
                    current.append(k)
        level += 1
        print("")


def zig_zag(node_list, root, num):
    count = 0
    level = 1
    current = [root]
    flag = True
    while count < num:
        if flag:
            print('Level %d from left to right:' % (level), end='')
        else:
            print('Level %d from right to left:' % (level), end='')
        for j in range(len(current)):
            node = current.pop(0)
            print(' %d' % (node), end='')
            count += 1
            if flag:
                if node_list[node - 1][0] != 0:
                    current.append(node_list[node - 1][0])
                if node_list[node - 1][1] != 0:
                    current.append(node_list[node - 1][1])
            else:
                if node_list[node - 1][1] != 0:
                    current.append(node_list[node - 1][1])
                if node_list[node - 1][0] != 0:
                    current.append(node_list[node - 1][0])
        if flag:
            flag = False
        else:
            flag = True
        current.reverse()
        level += 1
        print("")


line = input().strip()
nums = int(line.split()[0])
roo = int(line.split()[1])
nod_list = [[0, 0] for i in range(20)]
for i in range(nums):
    new_line = input().strip()
    nod_list[int(new_line.split()[0]) - 1][0] = int(new_line.split()[1])
    nod_list[int(new_line.split()[0]) - 1][1] = int(new_line.split()[2])
level_visit(nod_list, roo, nums)
zig_zag(nod_list, roo, nums)




