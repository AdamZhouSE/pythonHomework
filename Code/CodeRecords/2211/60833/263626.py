lines = []
while True:
    try:
        lines.append(input())
    except:
        break
list1=list(lines.pop(0).split(" "))
n=int(list1[0])
m=int(list1[1])
list_1st = list(lines.pop(0).split(" "))
First_letter=list_1st[0]
name=list_1st[0]
namelist=[]
namelist.append(name)
index=int(list_1st[1])
for i in range(1,n):
    list_run = list(lines.pop(0).split(" "))
    letter=list_run[0]
    number=int(list_run[1])
    name=letter+namelist[number-1]
    namelist.append(name)
for i in range(0,m):
    test=lines.pop(0)
    s=len(test)
    count = 0
    for j in namelist:
        if((len(j)>=s)&(test==j[0:s])):
            count=count+1
    print(count)
