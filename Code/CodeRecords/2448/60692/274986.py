a = input()[1:-1].split(",")
a = [int(i) for i in a]
a.sort()
mid = len(a) // 2
h = a[mid]
while len(a[mid:]) >= a[mid] and mid < len(a):
    mid += 1
while len(a[mid:]) < a[mid] and mid >= 0:
    mid -= 1
h = a[mid]
if h == 1:
    print(a)
print(h)