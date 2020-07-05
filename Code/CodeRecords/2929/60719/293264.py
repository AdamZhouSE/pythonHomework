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


limit = to_int_list(input(), " ")
this = []
for i in range(limit[0]):
    this.append(to_int_list(input(), " "))
sum = 0
for i in range(limit[0]):
    sum += this[i][0]
if sum <= limit[1]:
    print(0)
else:
    count = 0
    d = []
    for i in range(limit[0]):
        d.append(this[i][0]-this[i][1])
    d.sort(reverse=True)
    for i in range(len(d)):
        sum -= d[i]
        count += 1
        if sum <= limit[1]:
            break
    if count == len(d) and sum > limit[1]:
        print(-1)
    else:
        print(count)