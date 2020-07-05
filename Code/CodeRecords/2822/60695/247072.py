n = int(input())
a = input()
b = input()
aOriginal = a[2:].split(" ")
bOriginal = b[2:].split(" ")
n1 = a[0:1]
n2 = b[0:1]
a = a[2:].split(" ")
b = b[2:].split(" ")
count = 0
flag = False
while len(a) > 0 and len(b) > 0:
    if int(a[0]) > int(b[0]):
        a.append(b[0])
        a.append(a[0])
    else:
        b.append(a[0])
        b.append(b[0])
    b.remove(b[0])
    a.remove(a[0])
    count += 1
    if "".join(a) == "".join(aOriginal) and "".join(b) == "".join(bOriginal):
        t = "".join(a)
        p = "".join(aOriginal)
        flag = True
        break
if flag:
    print("-1")
else:
    if len(a) == n:
        print(str(count) + " 1")
    else:
        print(str(count) + " 2")