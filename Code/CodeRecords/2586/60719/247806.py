a = int(input())
b = int(input())
c = int(input())
if a < b:
    if a > c:
        tmp = a
        a = c
        c = b
        b = tmp
    elif b > c:
        tmp = c
        c = b
        b = tmp
else:
    if a < c:
        tmp = a
        a = b
        b = tmp
    elif c < b:
        tmp = a
        a = c
        c = tmp
    else:
        tmp = a
        a = b
        b = c
        c = tmp
m = min(b-a-1, 1)+min(c-b-1, 1)
n = c-a-2
if b-a == 2 or c-b == 2:
    m = 1
print("["+str(m)+", "+str(n)+"]")