tests = int(input())
for i in range(0,tests):
    ls = list(map(int,input().split(' ')))
    A = ls[0]
    B = ls[1]
    C = ls[2]
    print(pow(A,B)%C)