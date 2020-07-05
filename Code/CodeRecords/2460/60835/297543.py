'''
[Pi, Di, Ci] = [parent, number, money]
'''   
n = int(input())
group = []
graph = []
start = -1
for i in range(n):
    graph.append([])
for i in range(n):
    pi, di, ci = map(int, input().split())
    
