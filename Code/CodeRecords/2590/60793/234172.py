totalInput = int(input())
ls = []
for x in range(0, totalInput):
    ls .append(input())
for elem in ls:
    s = list(elem)
    s = tuple(s)
    if len(s)%2 == 0:
        print("HE!")
    else:
        print("HE!")