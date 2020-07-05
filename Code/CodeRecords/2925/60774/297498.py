n = int(input())
a = list(map(int,input().split(' ')))
b = list(map(int,input().split(' ')))
c = []
cur = -1
for car in a:
    if(b.index(car) > cur):
        cur = b.index(car)
    else:
        c.append(car)
print(len(c))