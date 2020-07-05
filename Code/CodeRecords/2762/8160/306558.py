def solve():
    num = int(input())

    for _ in range(num):
        input()
        arr = [i for i in input().split(' ')]
        arr2 = []

        for i in range(0, len(arr), 2):
            arr2.append([arr[i], int(arr[i+1])])

        calc(arr2)


def calc(arr):
    face = 0
    pos = [0, 0]

    for op in arr:
        if op[0] == 'U':
            face = face + 0
        elif op[0] == 'D':
            face = face + 2
        elif op[0] == 'L':
            face = face + 3
        elif op[0] == 'R':
            face = face + 1

        face = face % 4

        if face == 0:
            pos[1] = pos[1] + op[1]
        elif face == 1:
            pos[0] = pos[0] + op[1]
        elif face == 2:
            pos[1] = pos[1] - op[1]
        elif face == 3:
            pos[0] = pos[0] - op[1]

    distance = int(pow((pos[0]**2 + pos[1]**2),1/2))

    if face == 0:
        print(distance ,'N')
    elif face == 1:
        print(distance ,'E')
    elif face == 2:
        print(distance ,'S')
    elif face == 3:
        print(distance ,'W')


solve()
