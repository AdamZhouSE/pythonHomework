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
rec = []
for i in range(num):
    rec.append(to_int_list(input(), " "))
res = "YES"
temp = []
for i in range(num):
    if i == 0:
        temp.append(max(rec[0][1], rec[0][1]))
    else:
        m = max(rec[i][0], rec[i][1])
        if m <= temp[i-1]:
            temp.append(m)
        elif min(rec[i][0], rec[i][1]) > temp[i-1]:
            res = "NO"
            break
        else:
            temp.append(min(rec[i][0], rec[i][1]))
print(res)