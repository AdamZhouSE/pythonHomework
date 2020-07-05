def all_to_int(x):
    for i in range(len(x)):
        x[i] = int(x[i])
    return x


limit = input().split(" ")
limit = all_to_int(limit)
s = input()
n = int(input())
for i in range(n):
    ops = input().split(" ")
    ops = all_to_int(ops)
    s0 = s[ops[0]:ops[1]]
    s = s[:ops[2]]+s0+s[ops[2]:]
    if len(s) > limit[1]:
        s = s[:limit[i]]
print(s[:limit[0]])