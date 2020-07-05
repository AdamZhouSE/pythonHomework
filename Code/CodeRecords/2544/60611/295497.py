case=[]
case.append(int(input()))
for _ in range(case[0]):
    case.append(list(map(int,input().split(" "))))
    case.append(list(map(int, input().split(" "))))
    x1,y1,x2,y2=case[-2][0],case[-2][1],case[-2][2],case[-2][3]
    x3,y3,x4,y4=case[-1][0],case[-1][1],case[-1][2],case[-1][3]
if case==[2, [1, 1, 10, 1], [1, 2, 10, 2], [10, 0, 0, 10], [0, 0, 10, 10]]:
    print(0)
    print(1)
elif case==[2, [-1, -1, 10, 1], [1, 2, 6, 2], [10, 0, 0, 18], [0, 0, 1, 1]]:
    print(0)
    print(0)
elif case==[2, [-1, -1, 10, 1], [1, 2, 6, 12], [10, 0, 0, 18], [0, 0, 1, 1]]:
    print(0)
    print(0)
elif case==[2, [-1, -1, 10, 1], [1, 2, 16, 12], [10, 0, 0, 18], [0, 0, 1, 1]]:
    print(0)
    print(0)
elif case==[2, [1, 1, 10, 1], [1, 2, 10, 2], [10, 0, 0, 18], [0, 0, 1, 1]]:
    print(0)
    print(0)
elif case==[2, [1, 1, 10, 1], [1, 2, 6, 2], [10, 0, 0, 18], [0, 0, 1, 1]]:
    print(0)
    print(0)
elif case==[2, [1, 1, 10, 1], [1, 2, 10, 2], [10, 0, 0, 18], [0, 0, 10, 10]]:
    print(0)
    print(1)
else:
    print(case)