a = input()
x = input()
num = []
value = ''
for i in range(1, len(x) + 1):
    if x[i-1] != " ":
        value = value + x[i-1]
        continue
    else:
        num.append(value)
        value = ''
num.append(value)
value = ''

total = int(num[0])
ex = int(num[1])

y = input()
num1 = []
for i in range(1, len(y) + 1):
    if y[i-1] != " ":
        value = value + y[i-1]
        continue
    else:
        num1.append(value)
        value = ''
num1.append(value)
value = ''

unread = []
read = []
trash = []
for i in range(1,total + 1):
    unread.append(str(i))

for i in range(0,ex):
    value = num1[i*2+1]
    if num1[i*2] == '1':
        unread.remove(value)
        read.append(value)
    elif num1[i*2] == '2':
        read.remove(value)
        trash.append(value)
    elif num1[i*2] == '3':
        unread.remove(value)
        trash.append(value)
    elif num1[i*2] == '4':
        trash.remove(value)
        read.append(value)
    else :
        print("Error")
        break

if len(unread) == 0:
    print("EMPTY")
else:
    for i in range(0,len(unread)) :
        print(unread[i], end=" ")
print("")
if len(read) == 0:
    print("EMPTY")
else:
    for i in range(0,len(read)) :
        print(read[i], end=" ")
print("")
if len(trash) == 0:
    print("EMPTY")
else:
    for i in range(0,len(trash)) :
        print(trash[i], end=" ")
print("")