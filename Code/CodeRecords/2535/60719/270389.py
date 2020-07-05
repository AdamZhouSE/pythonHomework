a = input()
a = a[1: len(a)-1].split(",")
size = len(a)
maxres = 0
numinx = [0]*size
for index in range(size):
    a[index] = int(a[index])
    numinx[a[index]] = index
for index in range(size-1):
    flag = True
    for check in range(index):
        if numinx[check] > index:
            flag = False
            break
    if flag:
        maxres += 1
print(maxres)
