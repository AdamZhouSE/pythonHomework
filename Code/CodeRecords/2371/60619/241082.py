import re

t = int(input())
for index in range(t):
    string = input()
    ori = re.sub(r'\W', "", string).lower()
    i = 0
    j = len(ori)-1
    result = True
    while i < j:
        if ori[i] != ori[j]:
            result = False
            break
        i += 1
        j -= 1
    if result:
        print("YES")
    else:
        print("NO")