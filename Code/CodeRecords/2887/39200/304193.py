n = int(input())
passA = 0
passB = 0
failA = 0
failB = 0
for x in range(n):
    cmd = input().split()
    if cmd[0]=="1":
        passA += int(cmd[1])
        failA += int(cmd[2])
        
    else:
        passB += int(cmd[1])
        failB += int(cmd[2])
if passA >= failA:
    print("LIVE")
else:
    print("DEAD")
if passB >= failB:
    print("LIVE")
else:
    print("DEAD")

