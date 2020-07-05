def check():
    global fail1
    global pass1
    global fail2
    global pass2
    data = [int(j) for j in input().split(" ")]
    if data[0] == 1:
        pass1 += data[1]
        fail1 += data[2]
    else:
        pass2 += data[1]
        fail2 += data[2]


n = int(input())
pass1 = 0
fail1 = 0
fail2 = 0
pass2 = 0
for i in range(0, n):
    check()
if pass1 >= fail1:
    print("LIVE")
else:
    print("DEAD")
if pass2 >= fail2:
    print("LIVE")
else:
    print("DEAD")
