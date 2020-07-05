#27
def countX(s):
    count = 0
    n = len(s)
    for i in range(0,n):
        if i != 0 :
            if s[i] == "x":
                if s[i-1] >= "0" and s[i-1] <= "9":
                    if i-2 >= 0:
                        if s[i-2] == "+":
                            count += int(s[i-1])
                        if s[i-2] == "-":
                            count -= int(s[i-1])
                    else:
                        count += int(s[i-1])
                elif s[i-1] == "+":
                    count += 1
                elif s[i-1] == "-":
                    count -= 1
        else:
            if s[i] == "x":
                count += 1
    return count

eq = input().split("=")
lef = eq[0]
rig = eq[1]
outcome = 0
lValue = lef.replace("x","1*0")
rValue = rig.replace("x","1*0")
l = eval(lValue)
r = eval(rValue)
if l == r:
    if countX(lef) == countX(rig):
        print("Infinite solutions")
        exit(0)
    else:
        outcome = 0
        print("x=", end="")
        print(outcome)
else:
    val = r - l
    x = countX(lef) - countX(rig)
    if x == 0:
        print("No solution")
        exit(0)
    else:
        outcome = int(val/x)
        print("x=",end="")
        print(outcome)
