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
getin = to_int_list(input(), " ")
getout = to_int_list(input(), " ")
getin.reverse()
getout.reverse()
count = 0
for i in range(num):
    for j in range(i):
        if getin.index(getout[j]) > getin.index(getout[i]):
            count += 1
            break
print(count)