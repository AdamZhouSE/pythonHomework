num = int(input())
strs = input().split(' ')
color = [int(i) for i in strs]
clj = 0
dm = 0
turn = True
for i in range(num):
    if color[0]>=color[len(color)-1]:
        if turn:
            clj += color.pop(0)
        else:
            dm += color.pop(0)
    else:
        if turn:
            clj += color.pop()
        else:
            dm += color.pop()
    turn = not turn
print("{} {}".format(clj,dm))