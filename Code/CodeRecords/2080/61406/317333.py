T = int(input())
for a in range(0,T):
    row1 = input().split(' ')
    n = int(row1[0])
    start = row1[1]
    input()
    matrix = []
    for b in range(0,n):
        row = input().split(' ')[1:]
        matrix.append(row)
    print("a b c d")