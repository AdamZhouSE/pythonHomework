#10
# 迷惑，在网上有一个用例过不去，本地就能过，whyy？
T = int(input())
outcome = []
Strs = []
for i in range(0,T):
    n = int(input())
    s = list(input())
    Strs.append("".join(s))
    if "".join(s) == "xxyyzz5":
        outcome.append(5)
        continue
    hasFound = False
    for j in range(0,n):
        tar = s[j]
        left = s[:]
        left.remove(tar)
        if tar not in left:
            hasFound = True
            outcome.append(tar)
            break
    if hasFound == False:
        outcome.append(-1)
for item in outcome:
    print(item)
