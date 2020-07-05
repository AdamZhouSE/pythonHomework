alp = '0123456789abcdefghijklmnopqrstuvwxyz'
aNum = {}
for i in range(36):
    aNum.update({alp[i]: i})
T = eval(input())
for i in range(T):
    s1 = input()
    s2 = input()
    used1 = [False] * 36
    used2 = [False] * 36
    for j in range(len(s1)):
        used1[int(aNum[s1[j]])] = True
    for j in range(len(s2)):
        used2[int(aNum[s2[j]])] = True
    for j in range(36):
        if used1[j] != used2[j]:
            print(alp[j], end='')
print()
print()