num = int(input())
sets = list()
notes = list()
for i in range(num):
    str = input()
    notes.append(str)
    strs = list()
    for j in range(len(str)):
        if str[j]!=' ':
            strs.append(str[j])
    strs.sort()
    if not strs in sets:
        sets.append(strs)
#print(sets)
#if len(sets)==1:print(notes)
print(len(sets),end='')