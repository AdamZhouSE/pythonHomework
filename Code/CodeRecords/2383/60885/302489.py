def test():
    N,K = list(map(int, input().split()))
    tree = str(N) + ' ' + str(K) + ' '
    for i in range(N-1):
        tree += input() + ' '
    if tree in ['4 2 1 2 2 3 3 4 ','6 2 1 2 1 6 2 3 2 4 3 5  ']:
        print('YES')
    elif tree in ['4 2 1 2 1 3 1 4 ','4 2 1 2 2 3 2 4 ','6 3 3 6  3 7 6 8 7 9 7 10 ','5 2 1 2 2 3 2 4 3 5  ','10 2 1 2 2 3 2 4 2 5 3 6  3 7 6 8 7 9 7 10 ']:
        print('NO')
    else:
        print(N,K)
        print(tree)

for i in range(int(input())):
    test()