tests = input().split()
N = int(tests[0])
C = int(tests[1])
nodes = []
for i in range(0,pow(2,N)-1):
    nodes.append([0])
nodes[0]=[1,0]
for i in range(0,N-1):
    ls = input().split()
    start = int(ls[0])
    end = int(ls[1])
    index = 0
    for j in range(0,N):
        if nodes[j][0]==start:
            index = j
            break
    if nodes[index*2+1][0]==0:
        nodes[index*2+1][0]=end
    else:
        nodes[index*2+2][0]=end
for j in range(0,C):
    ls = input().split()
    com = ls[0]
    num = int(ls[1])
    index = 0
    for k in range(0,len(nodes)):
        if nodes[k][0]==num:
            index = k
            break
    if com=='Q':
        while len(nodes[index])==1:
            index = int((index-1)/2)
        print(nodes[index][0])
    else:
        nodes[index].append(0)
        