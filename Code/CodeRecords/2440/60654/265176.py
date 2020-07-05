a = list(input().lstrip("[").rstrip("]").split(","))
b = []
for i in a:
    b.append(int(i))
for i in range(b.__len__()-1):
    for j in range(i+1,b.__len__()):
        temp = i
        if b[temp] > b[j]:
            temp, j = j, temp
        b[i], b[temp] = b[temp], b[i]
print(b)
