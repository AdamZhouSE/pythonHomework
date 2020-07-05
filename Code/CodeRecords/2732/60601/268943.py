n = eval(input())
for i in range(n):
    line = input().split(' ')
    A = int(line[0])
    B = int(line[1])
    C = int(line[2])
    print(A**B%C)