m = input()
list0 = list(map(int,m.split(",")))
for i in range(len(list0)):
    if list0.count(list0[i])>=2:
        print(list0[i])
        break