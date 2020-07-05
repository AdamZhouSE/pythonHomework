import math
def isTriangle(list):
    if list[0] + list[1] > list[2] and list[1] + list[2] > list[0] and list[0] + list[2] > list[1]:
        return True
    else:
        return False
times = int(input())
result = 0
for i in range(times):
    result = 0
    edge = []
    n = int(input())
    line = input().split(" ")
    for j in range(len(line)):
        edge.append(int(line[j]))
    edge.sort()
    triangle = [0,0,0]
    for k in range(0,len(edge)-2):
        triangle[0] = edge[k]
        for m in range(k+1,len(edge)-1):
            triangle[1] = edge[m]
            for x in range(m+1,len(edge)):
                triangle[2] = edge[x]
                if isTriangle(triangle):
                    result += 1
    print(result)

