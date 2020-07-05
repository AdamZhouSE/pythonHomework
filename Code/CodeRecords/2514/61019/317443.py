read = lambda: eval(input())
read_line = lambda: [int(x) for x in input().split()]

xs = input()
ts = input()
loc1 = 0
loc2 = 0
while loc2 < len(ts):
    if xs[loc1] == ts[loc2]:
        loc1 += 1
        if loc1 == len(xs):
            print(True)
            exit(0)
    loc2 += 1
print(False)
