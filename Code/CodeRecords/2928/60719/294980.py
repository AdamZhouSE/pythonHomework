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


v = int(input())
nums = to_int_list(input(), " ")
m = v
s = 0
for i in range(9):
    if m >= nums[i]:
        m = nums[i]
        s = i + 1
remain = v % m
if v == 0:
    print(-1)
elif remain == 0:
    print(str(s)*(v//m))
elif remain == v:
    print(-1)
else:
    c = nums.copy()
    for j in range(s, 9):
        c[j] = c[j] - m
    i = 8
    can = []
    while i >= s:
        if remain - c[i] >= 0:
            remain -= c[i]
            can.append(i+1)
        else:
            i -= 1
    res = ""
    for k in can:
        res += str(k)
    res += (str(s)*(v//m-len(can)))
    print(res)