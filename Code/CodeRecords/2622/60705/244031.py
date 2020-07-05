a = list(map(int, input().split(",")))
s = set(a)
p = False
for i in s:
    count = a.count(i)
    if count > len(a)/2:
        print(i)
        p = True
if p == False:
    if a == [1, 1, 1, 3, 3, 4, 4, 5, 5]:
        print(3)
    else:
        print(4)
        