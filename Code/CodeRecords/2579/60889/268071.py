numOfLine = int(input())
mat = []
for i in range(numOfLine):
    line = input().split(",")
    line = list(map(int,line))
    mat.append(line)
threshold = int(input())
m = numOfLine
n = len(mat[0])
if m > n:
    edge = n
else:
    edge = m
isFind = False
while (edge!=0)and(not(isFind)):
    for i in range(m-edge+1):
        for j in range(n-edge+1):
            summary = 0
            for l in range(edge):
                for m in range(edge):
                    summary = summary + mat[i+l][j+m]
            if summary <= threshold:
                isFind = True
                break
        else:
            continue
        break
    else:
        edge = edge - 1
        continue
    break
print(edge)