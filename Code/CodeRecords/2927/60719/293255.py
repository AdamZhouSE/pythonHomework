def handle_each_use_case():
    enemy = to_int_list(input(), " ")
    if enemy[0] - me[1] > enemy[1]:
        return "NO"
    if enemy[0] + me[1] < enemy[1]:
        return "NO"
    if -enemy[0] + me[1] > enemy[1]:
        return "NO"
    if -enemy[0] + 2*me[0]-me[1] < enemy[1]:
        return "NO" 
    return "YES"


def str_to_list(l, split):
    l0 = l[1: len(l)-1].split(split)
    return l0


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


global me
me = to_int_list(input(), " ")
es = int(input())
for i in range(es):
    res = handle_each_use_case()
    print(res)
