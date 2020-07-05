def to_int(l):
    if l == []:
        print("no")
    for i in range(len(l)):
        l[i] = int(l[i])
    return l


limit = input().split(" ")
limit = to_int(limit)
if limit[1] == 0:
    print(limit)
a = to_int(input().split(" "))
for i in range(limit[1]):
    con = to_int(input().split(" "))
    sub = []
    for i in range(con[0]-1, con[1]):
        sub.append(a[i])
    sub.sort()
    print(sub[con[2]-1])