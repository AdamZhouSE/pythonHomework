a = [int(i) for i in input().split()]
a.sort()
spec_list = ["Bear", "Elephant", "Alien"]
res = spec_list[2]
if a[0] == a[1] == a[2] == a[3]:
    head, body = a[4], a[5]
elif a[1] == a[2] == a[3] == a[4]:
    head, body = a[0], a[5]
elif a[2] == a[3] == a[4] == a[5]:
    head, body = a[0], a[1]
else:
    head = 0
    body = -1
if head < body:
    res = spec_list[0]
elif head == body:
    res = spec_list[1]
else:
    res = spec_list[2]
print(res)
