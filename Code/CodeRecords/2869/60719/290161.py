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
nums = to_int_list(input(), " ")
count = [0.01]*num
for i in nums:
    if i in count:
        count.remove(i)
    count.append(i)
s = ""
while 0.01 in count:
    count.remove(0.01)
for i in range(len(count)):
    s += str(count[i])
    if i != len(count)-1:
        s += " "
print(len(count))
print(s)