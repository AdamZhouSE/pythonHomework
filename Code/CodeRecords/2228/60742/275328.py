target = int(input())
res = 0
steps = 0
while res<target:
    steps += 1
    res += steps
minus = res-target
if minus%2==0:
    print(steps)
else:
    if steps%2==0:
        print(steps+1)
    else:
        print(steps+2)