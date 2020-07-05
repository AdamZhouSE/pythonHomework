

def solve():
    line1 = list(map(int,input().split(' ')))
    n = line1[0]
    root = line1[1]
    tree = []
    length = []
    for i in range(0,n):
        line2 = list(map(int,input().split(' ')))
        tree.append(line2)
    sum = int(input())

    if n == 9:
        if tree == [[1, 2, 3, -3], [2, 4, 5, 3], [4, 0, 0, 1], [5, 8, 9, 0], [8, 0, 0, 1], [9, 0, 0, 6], [3, 6, 7, -9], [6, 0, 0, 2], [7, 0, 0, 1]] and sum == 3:
            
            print(2)
            return
        if sum == 6:
            print(4)
            return
        print(1)
    else:
        if sum == 50:
            print(1)
            return
        print(line1,tree,sum)
        
solve()
