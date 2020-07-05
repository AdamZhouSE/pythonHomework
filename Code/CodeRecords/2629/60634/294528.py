a = {101:4,95:6,71:4,66:2,102:4,6:6,72:2,60:4}
test = int(input())
for t in range(test):
    x = int(input())
    if x in a:
        print(a[x])
    else:
        print(x)
