x, y = list(input().split())
a1 = list(input().split())
b1 = []
for i in a1:
    b1.append(int(i))
for i in range(int(y)):
    a, b, c = list(input().split())
    b1[int(b)-1:int(c)].sort()
    if a == "1":
        b1[int(b)-1:int(c)].reverse()
print(b1[int(input())-1])