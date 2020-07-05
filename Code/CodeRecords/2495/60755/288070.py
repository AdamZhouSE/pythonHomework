def judge(a,b):
    flag = True
    s = list(b)
    all = list(a)
    for i in s:
        if all.count(i)>=s.count(i):
            flag = False
    return flag


s = input()
all = input()[2:-2].split("\",\"")
for i in all:
    if not judge(i, s):
        all.remove(i)
max = -1
for i in all:
    if len(i) > max:
        max = len(i)
for i in all:
    if len(i)!= max:
        all.remove(i)
all.sort()
print(all[0])