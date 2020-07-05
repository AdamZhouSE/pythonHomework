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
this = []
for i in range(limit):
    this.append(to_int_list(input(), " "))
count = 2
for i in range(1, limit-1):
    if this[i][0] - this[i][1] > this[i-1][0] or this[i][0] + this[i][1] < this[i+1][0]:
        count += 1
print(count)
