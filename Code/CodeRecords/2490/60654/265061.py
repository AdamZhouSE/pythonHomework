a = list(input().lstrip("[").rstrip("]").split(","))
b = list(input().lstrip("[").rstrip("]").split(","))
c = []
for i in a:
    if i in b and i not in c:
        c.append(int(i))
c.sort()        
print(c)
