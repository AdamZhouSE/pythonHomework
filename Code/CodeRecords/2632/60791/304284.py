n,m = [int(i) for i in input().split(' ')]

ml = 0
mr = n+1
cut = []
check = []
all_thing = []
for i in range(m):
    
    thing = input().split(' ')
    all_thing.append(thing)
    
    if thing[0] == 'R' :
        if len(cut) != 0:
            cut.pop()
    elif thing[0] == 'D':
        cut.append(int(thing[1]))
    else:
        trap = int(thing[1])
        left,right = -1,mr
        for item in cut:
            if item == trap:
                left = trap
                right = trap+1
                break;
            elif item < trap and left < item:
                left = item
            elif item > trap and right > item:
                right = item
        if left == -1:
            left = ml
        print(right - left - 1)
        check.append(right-left-1)
