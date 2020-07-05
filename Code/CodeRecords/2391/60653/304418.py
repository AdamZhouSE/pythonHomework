n = int(input())
a = []
index = []
for i in range(0, n):
    a.append(input())
    index.append(1)
m = int(input())
for i in range(0, m):
    s = input()
    if a.count(s) == 0:
        print("WRONG")
    elif index[a.index(s)] == 1:
        print("OK")
        index[a.index(s)] = 2
    elif index[a.index(s)] == 2:
        print("REPEAT")
    else:
        print("WRONG")
