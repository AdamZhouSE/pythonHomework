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


insnum = int(input())
count = [0, 0]
succ = [0, 0]
for i in range(insnum):
    ins = to_int_list(input(), " ")
    count[ins[0]-1] += 1
    succ[ins[0]-1] += ins[1]
if count[0]*10 <= succ[0]*2 and count[0] != 0:
    print("LIVE")
else:
    print("DEAD")
if count[1]*10 <= succ[1]*2 and count[1] != 0:
    print("LIVE")
else:
    print("DEAD")