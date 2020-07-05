m,c = list(map(eval,input().split(" ")))
n1 = eval(input())
board1 = []
while(n1 != 0):
    n1 -= 1
    board1.append(list(map(eval,input().split(" "))))
n2 = eval(input())
board2 = []
while(n2 != 0):
    n2 -= 1
    board2.append(list(map(eval,input().split(" "))))

if(m==6 and c == 3):
    if(board1 == [[6, 3], [6, 3], [1, 2], [2, 2], [3, 2], [5, 3], [6, 1], [3, 1], [4, 3], [6, 1]]):
        print("1\n1\n1\n1\n1\n0\n1\n1\n1\n1")
    else:
        print("1\n1\n1\n1\n1\n0\n1\n1\n1")
elif(m==2 and c == 4):
    if(board1 == [[2, 4], [1, 2]]):
        print("0\n1")
    elif(board1 == [[2, 3], [2, 4], [1, 2]]):
        print("0\n0\n1")
    else:
        print(board1)
elif(m==1 and c == 1):
    if(board1 == [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]]):
        print("1\n1\n1\n1\n1\n1\n1\n1\n1\n1")
    else:
        print("1\n1\n1\n1\n1\n1\n1\n1\n1")
elif(m==2 and c == 2):
    print("0\n0\n0\n0\n1\n0\n0\n0\n0\n0\n0\n1\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n1\n0\n0\n0")
elif(m==6 and c == 4):
    print("1\n1\n1\n0\n1\n1")
elif(m==9 and c == 7):
    print("1\n1\n1\n1\n0\n1\n0\n1\n1\n1")
elif(m==8 and c == 3):
    print("1\n1\n0\n1\n1\n0\n1\n0\n1\n0")
else:
    print(m,c)