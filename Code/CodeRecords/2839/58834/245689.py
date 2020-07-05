n = int(input())
names = []
for i in range(0,n):
    name = input()
    names.append(name)
print("NO")
for q in range(1,n):
    sign = True
    for w in range(0,q):
        if names[w] == names[q]:
            sign = False
    if sign:
        print("NO")
    else:
        print("YES")
n = int(input())
names = []
for i in range(0,n):
    name = input()
    names.append(name)
print("NO")
for q in range(1,n):
    sign = True
    for w in range(0,q):
        if names[w] == names[q]:
            sign = False
    if sign:
        print("NO")
    else:
        print("YES")
