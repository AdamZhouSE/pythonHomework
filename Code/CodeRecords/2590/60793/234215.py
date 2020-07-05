totalInput = int(input())
ls = []
for x in range(0, totalInput):
    ls .append(input())
for elem in ls:
    s = list(elem)
    s.sort()
    s1 = []
    for i in s:
        if not i in s1:
            s1.append(i)
    if len(s1)%2 == 0:
        print("SHE!")
    else:
        print("HE!")totalInput = int(input())
ls = []
for x in range(0, totalInput):
    ls .append(input())
for elem in ls:
    s = list(elem)
    s = tuple(s)
    if len(s)%2 == 0:
        print("SHE!")
    else:
        print("HE!")