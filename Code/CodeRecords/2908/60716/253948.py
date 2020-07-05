num = int(input())
sets = list()
for i in range(num):
    strs = input().split()
    temp = set(strs)
    if not temp in sets:
        sets.append(temp)
print(len(sets))
