a = list(map(int, input().split(",")))
s = set(a)
for i in s:
    count = a.count(i)
    if count > len(a)/2 - 1:
        print(i)
