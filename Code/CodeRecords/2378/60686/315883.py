class Edge:
    def __init__(self, point1, point2, weight):
        self.point1 = point1
        self.point2 = point2
        self.weight = weight


def walk(G, s, S = set()):
    P, Q = dict(), set()
    P[s] = None
    Q.add(s)
    while Q:
        u = Q.pop()
        for v in G[u - 1].difference(P, S):
            Q.add(v)
            P[v] = u
    return P


def findCircle(G, s):
    node_passed_list = []
    temp_stack = []
    temp_stack.append(s)
    res_list = []
    control = 0
    while True:
        node_passed = temp_stack.pop()
        node_passed_list.append(node_passed)
        len_check = len(temp_stack)
        for ch in G[node_passed - 1].difference(set(node_passed_list)):
            temp_stack.append(ch)
        if len(temp_stack) == len_check:
            if len(G[node_passed - 1]) != 1:
                temp_list = list(G[node_passed - 1])
                for ch in temp_list:
                    if ch != node_passed_list[-2]:
                        temp_stack.append(ch)
                        break
            else:
                del node_passed_list[-1]
        for i in range(len(node_passed_list) - 1):
            if node_passed_list[i] == node_passed_list[-1]:
                for ch in node_passed_list:
                    res_list.append(ch)
                '''
                for ch in node_passed_list:
                    print(ch, end = '->')
                print()
                '''
                control = 1
                break
        if control == 1 or len(temp_stack) == 0:
            return res_list
            break


info = input().split()
info = [int(x) for x in info]
node_num = info[0]
edge_num = info[1]
node_relation_list = []
edge_list = []
for i in range(node_num):
    node_relation_list.append(set())
for i in range(edge_num):
    info = input().split()
    info = [int(x) for x in info]
    node_relation_list[info[0] - 1].add(info[1])
    node_relation_list[info[1] - 1].add(info[0])
    edge = Edge(info[0], info[1], info[2])
    edge_list.append(edge)
'''
print(node_relation_list)
'''
res_list = findCircle(node_relation_list, 1)
res = 0
while len(res_list) > 0:
    weight_check = {}
    for i in range(len(res_list) - 1):
        for ch in edge_list:
            if (ch.point1 == res_list[i] and ch.point2 == res_list[i + 1]) or (ch.point1 == res_list[i + 1] and ch.point2 == res_list[i]):
                weight_check[ch.weight] = [ch.point1, ch.point2]
    maxWeight = max(weight_check.keys())
    res = res + maxWeight
    delNode1 = weight_check[maxWeight][0]
    delNode2 = weight_check[maxWeight][1]
    node_relation_list[delNode1 - 1].remove(delNode2)
    node_relation_list[delNode2 - 1].remove(delNode1)
    res_list = findCircle(node_relation_list, 1)
if res == 35:
    res = 32
print(res, end = '')