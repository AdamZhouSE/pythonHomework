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


num = int(input())
dis = []
for i in range(num):
    dis.append(to_int_list(input(), " "))
count = 0
for i in range(num):
    for j in range(i+1, num):
        if dis[i][0] == dis[j][0] or dis[i][1] == dis[j][1]:
            count += 1
print(count)