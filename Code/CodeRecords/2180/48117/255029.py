s1 = input()
s2 = input()
s1List = []


for count in range(1, len(s1) + 1):
    for i in range(len(s1)):
        if i + count <= len(s1):
            s1List.append(s1[i:i + count])

count = 0
for subStr in s1List:
    if subStr in s2 and s1.find(subStr) != s2.find(subStr):
        count += 1

print(count, end='')