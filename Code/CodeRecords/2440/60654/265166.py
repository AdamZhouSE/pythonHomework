a = list(input().lstrip("[").rstrip("]").split(","))
b = []
for i in a:
    b.append(int(i))
b.sort()
print(b)