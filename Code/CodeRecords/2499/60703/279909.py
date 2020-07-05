N = int(input())
Add = []
Query = []
Del = []
for i in range(N):
    l = input()
    this = l.split(" ")
    if(this[0]=="Add"):
        # a,b,c = [int(x) for x in this[1:]]
        if("" in this):
            this.remove("")
        a,b,c = int(this[1]),int(this[2]),int(this[3])
       # print(this)
        Add.append([a,b,c,True])
    if(this[0]=="Del"):
        de = int(this[1])
        Add[de-1][3] = False

    if(this[0]=="Query"):
        x = int(this[1])
        res = 0
        for inner in Add:
            if(inner[3]==True):
                a, b, c = inner[:-1]
                if(a*x+b>c):
                    res+=1
        print(res)