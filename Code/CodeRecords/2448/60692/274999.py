a = input()[1:-1].split(",")
a = [int(i) for i in a]
a.sort()
mid = len(a) // 2
h = a[mid]
while len(a[mid:]) >= a[mid]:
    h = a[mid]
    if mid + 1 < len(a):
        mid += 1
    else:
        break
while mid >= 0 and len(a[mid:]) < a[mid]:
    mid -= 1
h = a[mid]
print(h)
