def all_to_int(x):
    for i in range(len(x)):
        x[i] = int(x[i])
    return x


def str_to_list(l, split):
    l0 = l[1: len(l)-1].split(split)
    return l0


s = input()
s = str_to_list(s,",")
s = all_to_int(s)
i = 0
dec = 0
n = len(s)
for i in range(n):
    dec += (s[i]*(2**(n-1-i)))
print(dec)