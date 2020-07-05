data = list(map(int, input().split(',')))
can = True
if len(data) == 1:
    print(False)
    can = False
num = []
for i in list(set(data)):
    num.append(data.count(i))
x = min(num)
for i in num:
    if i % x != 0:
        print(False)
        can = False
        break
if can:
    print(True)
