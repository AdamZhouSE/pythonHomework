ls = list(map(int, input()[1:-1].split(",")))
count = 0
flag = False
if ls[-2] != ls[-1]:
    print(ls[-1])
else:
    for i in range(1, len(ls)):
        if ls[i - 1] != ls[i]:
            if count == 0:
                print(ls[i - 1])
                flag = True
            count = 0
        count += 1
if not flag:
    print(ls)