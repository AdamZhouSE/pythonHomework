s = input()
set1 = set()
num = []
label = []
for i in range(len(s)):
    size = len(set1)
    set1.add(s[i])
    if size != len(set1):
        label.append(s[i])
        num.append(s.count(s[i]))
for i in range(len(num)):
    max = num[i]
    index = i
    for j in range(i,len(num)):
        if max < num[j]:
            index = j
            max = num[j]
    if index != i:
        temp1 = num[index]
        num[index] = num[i]
        num[i] = temp1
        temp2 = label[index]
        label[index] = label[i]
        label[i] = temp2
for i in range(len(label)):
    for j in range(num[i]):
        print(label[i],end="")
print()