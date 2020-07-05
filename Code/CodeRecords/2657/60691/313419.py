line = input().split(' ')
N = int(line[0])
Q = int(line[1])
#[id,father,isOk]
Node = []
for i in range(N):
    Node.append([i+1,i+1,0])
for i in range(N-1):
    line = input().strip()
    line = list(map(int,line.split(' ')))
    Node[line[1]-1][1] = line[0]
Node[0][2] = 1#将根标记
#print(Node)
for i in range(Q):
    line = input().split(' ')
    opre = line[0]
    onum = int(line[1])
    if opre == 'C':
        Node[onum-1][2] = 1
    else:
        if Node[onum-1][2] == 1:
            print(onum)
        else:
            while onum!=1:
                onum = Node[onum-1][1]
                if Node[onum - 1][2] == 1:
                    print(onum)
                    break
                else:
                    continue
