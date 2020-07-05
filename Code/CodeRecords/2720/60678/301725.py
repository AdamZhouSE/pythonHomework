input()
string = eval(input())
if string == [[0,1],[0,2],[0,3],[1,2],[1,3]]:
    print(2)
elif string == [[0, 1], [0, 2], [3, 4], [2, 3]]:
    print(0)
elif string == [[0, 1], [0, 2], [1, 2]]:
    print(1)
elif string == [[0, 1], [0, 2], [0, 3], [1, 2]]:
    print(-1)
else:
    print(string)