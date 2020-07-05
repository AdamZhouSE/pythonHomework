n,d=map(int,input("").split(" "))
heightlist=list(map(int,input("").split(" ")))
team=0
for height1 in heightlist:
    for height2 in heightlist:
        if abs(height1-height2)<=d:
            team+=1
print(team-n)