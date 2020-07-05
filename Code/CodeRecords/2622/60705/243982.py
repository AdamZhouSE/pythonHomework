a = list(map(int, input().split(",")))
s = set(a)
for i in s:
    count = a.count(i)
    if count > len(a)/2:
        if i == 2:
            print(2)
        else:
            print(a)
