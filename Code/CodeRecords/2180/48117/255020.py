s1 = input()
s2 = input()
s1List = []
s2List = []

for count in range(1, len(s1) + 1):
    for i in range(len(s1)):
        if i + count <= len(s1):
            s1List.append(s1[i:i + count] + str(i) + str(i + count))


for count in range(1, len(s2) + 1):
    for i in range(len(s2)):
        if i + count <= len(s2):
            s2List.append(s2[i:i + count] + str(i) + str(i + count))


count = 0
for sub1 in s1List:
    for sub2 in s2List:
        if sub1 != sub2:
            if sub1[:-2] == sub2[:-2]:
                count += 1
print(count, end='')