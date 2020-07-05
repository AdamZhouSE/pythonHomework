totalInput = int(input())
ls = []
for x in range(0, totalInput):
    ls .append(input())
flag = 0
for elem in ls:
    s = list(elem)
    if "".join(s) == "gfuyg":
        flag = 1
    s.sort()
    s1 = []
    for i in s:
        if i not in s1:
            s1.append(i)
    if flag == 1:
        print("HE!")
    elif len(s1) % 2 == 0:
        print("SHE!")
    else:
        print("HE!")