a = input()
b = []
count = 0
for i in a:
    if i == '0':
        b.insert(0, 0)
    elif i == '2':
        count = count+1
    elif i == '1':
        b.append(1)
for i in range(count):
    b.append(2)
print(b)
