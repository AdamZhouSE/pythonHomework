'''给定一颗二叉树，分别实现按层和 ZigZag 打印二叉树。 ZigZag遍历: 意思是第一层从左到右遍历，第二层从右到左遍历，依次类推'''

def solve():
    line1 = input().split(' ')
    n = int(line1[0])
    root = int(line1[1])
    data = [[root]]
    final = [[root]]
    for i in range(0,n):
        line = list(map(int,input().split(' ')))
        if line[0] == root:
            final.append([line[1],line[2]])
            continue
        for j in range(0,len(final)):
            if line[0] in final[j] and j < len(final) - 1:
                if line[1] == 0 and line[2] != 0:
                    final[j + 1].append(line[2])
                elif line[2] == 0 and line[1] != 0:
                    final[j + 1].append(line[1])
                elif line[1] != 0 and line[2] != 0:
                    final[j + 1].append(line[1])
                    final[j + 1].append(line[2])
                break
            elif j == len(final) - 1:
                if line[1] != 0 and line[2] != 0:
                    final.append([line[1], line[2]])
                    break
                if line[1] != 0 and line[2] == 0:
                    final.append([line[1]])
                    break
                if line[1] == 0 and line[2] != 0:
                    final.append([line[2]])

    for i in range(0,len(final)):
        print('Level {0} : '.format(i + 1),end='')
        for j in range(0,len(final[i])):
            if j == len(final[i]) - 1:
                print(final[i][j])
            else:
                print(final[i][j], end=' ')

    for i in range(0,len(final)):
        if i % 2 == 0:
            print('Level {0} from left to right: '.format(i + 1),end='')
            for j in range(0, len(final[i])):
                if j == len(final[i]) - 1:
                    print(final[i][j])
                else:
                    print(final[i][j], end=' ')
        else:
            print('Level {0} from right to left: '.format(i + 1),end='')
            for j in range(len(final[i]) - 1, -1,-1):
                if j == 0:
                    print(final[i][j])
                else:
                    print(final[i][j], end=' ')

solve()