import math

x=int(input())
y=int(input())
bound=int(input())
if bound==0:
    print([])
else:
    xUp = int(math.log(bound, x)) + 1
    rlist = []
    for i in range(2, bound + 1):
        for j in range(0, xUp):
            rest = int(i - math.pow(x, j))
            if rest == 1 or (rest > 0 and round(math.log(rest, y)) == math.log(rest, y)):
                rlist.append(i)
                break
    print(rlist)