n = int(input())
ser1 = [0,0]
ser2 = [0,0]
ser = [ser1,ser2]
for j in range(n):
    ping = [int(i) for i in input().split()]
    if ping[0] == 1:
        ser1[0] +=ping[1]
        ser1[1] +=ping[2]
    if ping[0] == 2:
        ser2[0] +=ping[1]
        ser2[1] +=ping[2]
for i in ser:
    if i[0]<i[1]:
        print("DEAD")
    if i[0]>=i[1]:
        print("LIVE")