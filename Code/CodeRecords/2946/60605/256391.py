ori = input()
cnt = 0
toBeFound = "0"

for i in range(len(ori)-1, -1, -1):
    if ori[i] == toBeFound:
        cnt += 1
        if toBeFound == "0": toBeFound = "1"
        else: toBeFound = "0"

print(cnt, end="")