NumOfEg = int(input())
result = []
for i in range(NumOfEg):
    player = input().split(" ")
    a = 0
    b = 0
    while player[2] != "1":
        if int(player[0])%int(player[2]) == 0:
            player[0] = str(int(player[0]) - 1)
            a = a + 1
        if int(player[1])%int(player[2]) == 0:
            player[1] = str(int(player[1]) - 1)
            b = b + 1
        player[2] = str(int(player[2]) - 1)
    result.append(str(a)+" "+str(b))
for k in result:
    print(k)