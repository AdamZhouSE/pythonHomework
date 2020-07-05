import re
n = input().replace('.', '')
cgirl, cboy = 0, 0
for i in range(0, len(n)):
    for j in range(i, len(n)):
        if n[i:j + 1] == 'girl':
            cgirl += 1
        elif n[i:j + 1] == 'boy':
            cboy += 1

s = re.split(r"girl|boy", n)
result = [x.strip() for x in s if x.strip()!='']
for i in range(0, len(result)):
    if result[i] in "girl":
        cgirl += 1
    elif result[i] in "boy":
        cboy += 1
    elif result[i][0] in "girl":
        cgirl += len(result[i])
    elif result[i][0] in "boy":
        cboy += len(result[i])
print(cboy)
print(cgirl,end='')