number=int(input())
lists=[]
save=[]
for i in range(number):
    a=input()
    y=a.split(" ")
    if("" in y):
        y.pop(y.index(""))
    if(y[0]=="Add"):
        lists.append([int(y[1]),int(y[2]),int(y[3])])
        save.append([int(y[1]),int(y[2]),int(y[3])])
    elif(y[0]=="Del"):
        lists.pop(lists.index(save[int(y[1])-1]))
    elif(y[0]=="Query"):
        count=0
        x=int(y[1])
        for a in lists:
            if(x*a[0]+a[1]>a[2]):
                count=count+1
        print(count)
        