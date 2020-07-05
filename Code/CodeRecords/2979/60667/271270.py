li = input().split()
length = []
for i in li:
    length.append(len(i))
ind = length.index(max(length))
print(li[ind])