import sys


def execute(A,B):
    liA = list(A)
    liA.pop()  #去掉换行符
    liB = list(B)
    liB.pop()
    N = len(liB)
    count = 0
    for i in range(0,len(liA)-N):
        if liB == liA[i:i+N]:
            count += 1
    return count


Input = []
for line in sys.stdin:
    if line.strip() == '':
        break
    Input.append(line)

A = Input[0]
B = Input[1]
print(execute(A,B))