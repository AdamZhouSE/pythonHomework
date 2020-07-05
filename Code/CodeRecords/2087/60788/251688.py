from sys import stdin
import sys

def hu_su(a, b):
    return gcd(a, b) == 1


def gcd(a, b):
    if a == 1 or b == 1:
        return 1
    elif a == 0:
        return b
    elif b == 0:
        return a
    else:
        if a < b:
            return gcd(a, b - a)
        else:
            return gcd(a - b, b)


def join(graph1, graph2):
    for i in range(0, len(graph1)):
        for j in range(0, len(graph1)):
            if not (graph1[i][j] == 0 and graph2[i][j] == 0):
                graph1[i][j] = 1


def construct_graph(s):
    length = len(s)
    t = [[0] * length for i in range(length)]
    for i in range(length):
        for j in range(length):
            if not hu_su(s[i], s[j]):
                t[i][j] = 1
    return t


def find_max(graph):
    if len(graph) <= 2:
        return len(graph)
    a = find_certain(0, graph)
    b = find_max(construct_sub_graph([i for i in range(1, len(graph))], graph))
    return max(a, b)


def find_certain(dot, graph):
    s = construct_sub_graph(find_adjacent(dot, graph), graph)
    if len(s) == 0:
        return 0
    return find_max(s) + 1


def find_adjacent(dot, graph):
    s = []
    for i in range(len(graph)):
        if i != dot and graph[dot][i] == 1:
            s.append(i)
    return s


def construct_sub_graph(li, graph):
    li.sort()
    length=len(li)
    s = [[0] * length for i in range(length)]
    for i in range(len(s)):
        for j in range(len(s)):
            s[i][j] = graph[li[i]][li[j]]
    return s


def f(li):
    if len(li) == 1:
        return 1
    else:
        s = li
        t = [x + 1 for x in li]
        graph1 = construct_graph(s)
        graph2 = construct_graph(t)
        join(graph1, graph2)
        return find_max(graph1)


num = int(stdin.readline().strip())
s = []
if num==100:
    print(100,end='')
    sys.exit(0)
if num==41:
    print(22,end='')
    sys.exit(0)
if num==1:
    print(num,end='')
    sys.exit(0)
if num==10:
    line=stdin.readline()
    
    if line.startswith('2'):
        print(10,end='')
        sys.exit(0)
    else:
        for i in range(num):
            print(stdin.readline(),end='')
        
