string = input().strip().split("e")
isDi = True
if len(string) > 2:
    isDi = False
for k in string:
    start = 0
    if k.count(".")>1:
        isDi = False
    if k[0] == "-" or k[0] == "+":
        start = 1
    for i in range(start, len(k)):
        if not ("0" <= k[i] <= "9" or k[i] == "."):
            isDi = False
            break
    if not isDi:
        break
print(isDi)