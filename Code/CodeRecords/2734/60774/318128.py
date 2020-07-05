s = input().split()
n = int(s[0])
c = int(s[1])
m = int(s[2])
garden = list(map(int,input().split()))
for i in range(0,m):
    pick = []
    trip = input().split()
    l = int(trip[0])
    r = int(trip[1])
    temp = garden[l - 1:r]
    for f in temp:
        if(temp.count(f) > 1 and f not in pick):
            pick.append(f)
    print(len(pick))