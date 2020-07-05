def all_to_int(x):
    while "null" in x:
        x.remove("null")
    for i in range(len(x)):
        x[i] = int(x[i])
    return x


def str_to_list(l, split):
    l0 = l[1: len(l)-1].split(split)
    return l0


def handle_each_use_case():
    n = int(input())
    if n % 5 == 0:
        return -1
    return n % 5


bin = input().split(" ")
bin = all_to_int(bin)
s = [1]*(bin[1]+1)
for i in range(1, bin[1]+1):
    s[i] = s[i-1]**bin[0]+1
print(s[bin[1]]-s[bin[1]-1], end="")