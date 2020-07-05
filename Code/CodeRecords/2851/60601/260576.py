n = eval(input())
point = []
for i in range(n):
    point.append(list(map(int,input().split(' '))))
a = -1
b = 1
while True:
    isIn = True
    for i in point:
        if i[1] <= a * i[0] + b:
            continue
        else:
            isIn = False
            break
    if isIn:
        break
    else:
        b = b + 1
print(b)