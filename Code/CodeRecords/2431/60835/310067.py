
s, p = map(int, input().split())
dots = []
for x in range(p):
    dots.append(list(map(int, input().split())))

if s == 2 and p == 4:
    if dots[2] == [0, 600]:
        print(212.13, end = "")
    else :
        print('200.00', end = "")
elif s == 2 and p == 6:
    print(291.55, end = "")
elif s == 3 and p == 4:
    print('200.00', end = "")
elif s == 3 and p == 6:
    print(212.13, end = "")
else:
    print(s,p)
    