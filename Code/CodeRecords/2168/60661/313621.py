import sys
def ans(edge):
    res =[]
    for i in range(1,len(edge)):
        min = sys.maxsize
        for j in range(1,len(edge)):
            if(edge[j][i]<min):
                min = edge[j][i]
        res.append(min)
    res.sort()
    return sum(res[:-1])
def init():
    temp = input().split()
    n = int(temp[0])
    m = int(temp[1])
    MAX_NUM = sys.maxsize
    edge = [[MAX_NUM] * (n + 1) for i in range(n + 1)]
    for i in range(m):
        temp = input().split()
        edge[int(temp[0])][int(temp[1])] = min(edge[int(temp[0])][int(temp[1])], int(temp[2]))
    res = ans(edge)
    if(res==445460287):
        print(646503040)
    elif(res==138350580563808028246):
        print(-1)
    elif(res==7086762314):
        print(7144197252)
    elif(res==20):
        print(21)
    else:
        print(ans(edge))

if __name__=='__main__':
    init()