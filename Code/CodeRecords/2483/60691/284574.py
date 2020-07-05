def findchar(s1, s2):
    position = []
    iscontains = False
    for i in range(len(s2)):
        for j in range(len(s1)):
            if s2[i] == s1[j]:
                position.append(j)
                iscontains = True
                break

    if iscontains:
        position.sort()
        return s1[position[0]]
    else:
        return "$"



n = int(input())
s1 = []
s2 = []
for i in range(n):
    s1.append(input())
    s2.append(input())

for i in range(n):
    print(findchar(s1[i], s2[i]))