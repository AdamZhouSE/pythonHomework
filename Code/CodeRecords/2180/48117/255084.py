s1 = input()
s2 = input()
s1List = []


for count in range(1, len(s1) + 1):
    for i in range(len(s1)):
        if i + count <= len(s1):
            s1List.append(s1[i:i + count] + str(i))

count = 0
for subStr in s1List:
    index = int(subStr[-1])
    if subStr[:-1] in (s2[:index] + s2[index + 1:]):
        count += (s2[:index] + s2[index + 1:]).count(subStr[:-1])

print(count, end='')