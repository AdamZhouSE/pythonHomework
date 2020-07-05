def do(r:int):
    count = 0
    if r <= 1:
        return 0
    for w in range(1,2*r):
        for h in range(1,2*r):
            if (h/2)**2 + (w/2)**2 <= r**2:
                count += 1
    return count

test = int(input())
for i in range(test):
    r = int(input())
    print(do(r))