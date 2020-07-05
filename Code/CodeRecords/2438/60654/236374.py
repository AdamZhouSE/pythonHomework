s1 = input().strip("[").strip("]").split(",")
result = []
for i in range(s1.__len__()-1):
    for j in range(i+1, s1.__len__()):
        if s1[i] > s1[j]:
            temp = s1[i]
            s1[i] = s1[j]
            s1[j] = temp
for i in s1:
    result.append(int(i))
print(result)
