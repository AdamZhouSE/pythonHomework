T = eval(input())
N = []
Cell = []
K = []
mul = 1
for i in range(T):
    N.append(eval(input()))
    Cell.append(input())
    K.append(eval(input()))
#print(N)
#print(Cell)
#print(K)
for i in range(T):
    for j in range(N[i]):
        if j%2 == 0:
            mul *= int(Cell[i][j])
    print(mul%K[i])
    mul = 1