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
count = [0]
for i in range(1, limit-1):
    if this[i][0] - this[i][1] > this[i-1][0] or this[i][0] + this[i][1] < this[i+1][0]:
        count.append(i)
count.append(limit-1)
way = ["left"]
total = 2
for i in range(1, len(count)-1):
    if this[count[i]][0] - this[count[i]][1] > this[count[i]-1][0]:
        if count[i]-1 == count[i-1]:
            if way[i-1] == "right":
                if this[count[i]][0] - this[count[i]-1][0] >= this[count[i]][1] + this[count[i]-1][1]:
                    total += 1
                    way.append("left")
                else:
                    way.append("not")
            else:
                way.append("left")
                total += 1
        else:
            way.append("left")
            total += 1
    else:
        way.append("right")
        total += 1
print(total)
