import copy
s = input().split()
n = int(s[0])
m = int(s[1])
t = int(s[2])
done = []
rooms = [[] for i in range(1,m)]
rooms.insert(0,[i for i in range(1,n + 1)])
free = []
for i in range(0,t):
    order = input().split()
    if(order[0] == 'C'):
        i = int(order[1])
        j = int(order[2])
        if(i not in free):
            for r in rooms:
                if(i in r):
                    r.remove(i)
                    free.append(i)
                    break
        rooms[j - 1].append(i)
        free.remove(i)
    elif(order[0] == 'W'):
        l = int(order[1])
        r = int(order[2])
        temp = []
        points = 0
        for tp in range(l - 1,r):
            temp = copy.deepcopy(rooms[tp])
            temp.sort()
            if(temp not in done):
                done.append(temp)            
                points = points + len(temp)
        print(points)
            