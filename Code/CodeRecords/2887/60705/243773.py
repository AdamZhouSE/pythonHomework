n = int(input())
success_1 = 0
fail_1 = 0
success_2 = 0
fail_2 = 0

for i in range(0, n):
    line = list(map(int, input().split(" ")))
    if line[0] == 1:
        success_1 += line[1]
        fail_1 += line[2]
    else:
        success_2 += line[1]
        fail_2 += line[2]

if success_1 >= fail_1:
    print("LIVE")
else:
    print("DEAD")

if success_2 >= fail_2:
    print("LIVE")
else:
    print("DEAD")

