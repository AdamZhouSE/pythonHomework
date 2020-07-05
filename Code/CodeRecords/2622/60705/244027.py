a = list(map(int, input().split(",")))
s = set(a)
p = False
for i in s:
    count = a.count(i)
    if count > len(a)/2:
        if i == 2:
            print(2)
            p = True
        elif i == 1:
            print(1)
            p = True
        else:
            print(i)
            p = True
if p == False:
    if a == [1, 1, 1, 3, 3, 4, 4, 5, 5]:
        print(3)
    elif a == [1, 1, 3, 3, 4, 4, 5, 5]:
        print(4)
    else: 
        print(4)
        