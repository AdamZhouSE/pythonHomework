s = []
x, y = 0, 0
for i in range(5):
    subs = list(map(int, input().split()))
    if subs.count(1)==1:
        x=subs.index(1)
        y=i
print(abs(x-2)+abs(y-2))