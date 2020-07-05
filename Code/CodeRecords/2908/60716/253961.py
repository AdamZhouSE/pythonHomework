num = int(input())
sets = list()
for i in range(num):
    str = input()
    strs = list()
    for j in range(len(str)):
        if str[j]!=' ':
            strs.append(str[j])
    temp = set(strs)
    if not temp in sets:
        sets.append(temp)
#print(sets)
print(len(sets),end='')