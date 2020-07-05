x, y = list(input().split())
a1 = list(input().split())
b1 = []
for i in a1:
    b1.append(int(i))
for i in range(int(y)):
    a, b, c = list(input().split())
    c1 = b1[int(b)-1:int(c)]
    c1.sort()
    b1[int(b) - 1:int(c)] = c1
    if a == "1":
        c1 = b1[int(b) - 1:int(c)]
        c1.reverse()
        b1[int(b) - 1:int(c)] = c1
print(b1[int(input())-1])