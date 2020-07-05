a = list(map(int, input()[1:-1].split(",")))
s = set(a)
for i in s:
    count = a.count(i)
    if count > len(a)/2:
        print(i)
        break
