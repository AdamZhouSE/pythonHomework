


def execute(A,B):
    liA = list(A)
    #liA.pop()  #去掉换行符
    liB = list(B)
    #liB.pop()
    N = len(liB)
    count = 0
    for i in range(0,len(liA)-N+1):
        if liB == liA[i:i+N]:
            count += 1
    return count

A = input()
B = input()

print(execute(A,B),end="")