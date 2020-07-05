list=input().split(",")
Al,Li=0,0
l=len(list)
for i in range(len(list)): list[i]=int(list[i])
for i in range(l):
    if i%2==0:
        if list[0]>list[-1]:
            Al+=list[0]
            list.pop(0)
        else:
            Al+=list[-1]
            list.pop(-1)
    else:
        if list[0] > list[-1]:
            Li += list[0]
            list.pop(0)
        else:
            Li += list[-1]
            list.pop(-1)
if Al>Li:print(True)
else:print(False)