ori = input().replace(" ", "").split("=")
names = eval(ori[1][:len(ori[1])-2])
k = int(ori[2][0])
t = int(ori[3][0])
result = False
for i in range(len(names) - 1):
    for j in range(i + 1, min(len(names), i + k + 1)):
        if abs(names[i] - names[j]) <= t:
            result = True
            break
    if result:
        break
if result:
    print("true")
else:
    print("false")