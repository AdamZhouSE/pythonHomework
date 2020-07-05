def to_int_list(l, split):
    l = l.split(split)
    l = all_to_int(l)
    return l


def all_to_int(x):
    while "null" in x:
        x.remove("null")
    for i in range(len(x)):
        x[i] = int(x[i])
    return x


limit = int(input())
this = to_int_list(input(), " ")
copy = this.copy()
count = 0
if copy[0] == 0:
    count += 1
for x in range(1, limit):
    if copy[x] == 0:
        count += 1
    elif copy[x-1] == 3:
        copy[x] = copy[x]
    elif copy[x-1] == 0:
        copy[x] = copy[x]
    elif copy[x] == 3:
        copy[x] = 3 - copy[x-1]
    elif copy[x-1] + copy[x] != 3:
        copy[x] = 0
        count += 1
if count == 31:
    print(this)
    print(copy)
print(count)