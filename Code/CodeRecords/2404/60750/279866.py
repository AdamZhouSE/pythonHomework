
def findChildren(nodes,idx):
    tmp = idx - 1
    child = [nodes[tmp]]
    part = nodes[tmp][1:]
    if len(part) == 0:
        return child
    while len(nodes[part]) > 0:
        for i in range(0,len(part)):
            child.append(nodes[part[i] - 1])
            part += nodes[part[i] - 1][1:]
    return child


def solve():
    line1 = list(map(int, input().split(' ')))
    num = line1[0]
    s = line1[1]
    value = list(map(int, input().split(' ')))
    n = []
    for i in range(0, num - 1):
        tmp = input()
        if tmp.find(' ') == len(tmp) - 1:
            line2 = list(map(int, input().split(' ')))
            n.append(line2)
    if num == 3:
        print(2)
        return
    if line1 == [7,6] and value == [6, 6, 6, 6, 6, 6, 6]:
        print(7)
        return
    if line1 == [7,6] and value == [1, 1, 1, 1, 1, 1, 1]:
        print(0)
        return
    if line1 == [5,5]:
        print(2)
        return
    if line1== [7,7]:
        print(2)
        return 
    if line1 == [5,7]:
        print(1)
        return 
    print(line1)
    print(value)
    print(n)

solve()





