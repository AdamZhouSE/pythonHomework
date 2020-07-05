num = input().split()
N = int(num[0])
Q = int(num[1])
array = [[0, False] for _ in range(N)]
array[0][1] = True
for i in range(N - 1):
    temp = input().split()
    u = int(temp[0]) - 1
    v = int(temp[1]) - 1
    array[v][0] = u
for i in range(Q):
    temp = input().split()
    num = int(temp[1]) - 1
    if temp[0] == 'C':
        array[num][1] = True
    else:
        while not array[num][1]:
            num = array[num][0]
        print(num)
