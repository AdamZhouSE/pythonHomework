temp1 = list(input()[2:-2].split("],["))
ls = [list(map(int, x.split(","))) for x in temp1]
t1, t2, t3 = int(input()), int(input()), int(input())
result = []
for x in ls:
    if (t1 == 1 and x[2] == 0) or x[3] > t2 or x[4] > t3:
        continue
    result.append(x)
print(result)
print(temp1)