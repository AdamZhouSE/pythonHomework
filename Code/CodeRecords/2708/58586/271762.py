people,rooms,nums=map(int,input().split(" "))
room=[[p+1 for p in range(people)]]
for i in range(rooms-1):
    room.append([])
used=[]
for i in range(nums):
    operator=list(map(str,input().split(" ")))
    if operator[0]=="C":
        p,to=int(operator[1]),int(operator[2])
        for r in range(len(room)):
            if p in room[r]:
                room[r].remove(p)
                break
        room[to-1].append(p)
        room[to-1].sort()
    elif operator[0]=="W":
        begin,end=int(operator[1]),int(operator[2])
        sum=0
        for i in range(begin-1,end):
            if room[i] in used:
                continue
            else:
                if len(room[i])>0:
                    sum+=len(room[i])
                    used.append(room[i].copy())
        print(sum)