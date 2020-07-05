li = []

try:
    while True:
        item = input()
        li.append(item)
except EOFError:
    pass

li.sort()
for i in li:
    print(i)