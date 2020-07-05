ori = list(input())
i = 0
j = len(ori)-1
while i < j:
    if ori[i] == "-":
        i += 1
    else:
        temp = ori[j]
        ori[j] = ori[i]
        ori[i] = temp
        i += 1
        j -= 1
ori = ''.join(ori)
print(int(ori))