nm = input().split(" ")
n = int(nm[0])
m = int(nm[1])
a = input()
a = list(map(int, a.split(" ")))

for i in range(m):
    s = input().split(" ")
    s = list(map(int, s))
    l, r = s[1], s[2]
    front, back, middle = [], [], []
    for i in range(0, l - 1):
        front.append(a[i])
    for i in range(l - 1, r):
        middle.append(a[i])
    for i in range(r, len(a)):
        back.append(a[i])
    if s[0] == 1:
        middle = sorted(middle, reverse=True)
    else:
        middle = sorted(middle)
    front.extend(middle)
    front.extend(back)
    a = front
q = int(input())
print(a[q-1])
