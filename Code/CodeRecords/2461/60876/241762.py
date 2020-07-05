import sys
list=sys.stdin.readline().split(",")
newlist=[]
for item in list:
    newlist.append(int(item))
newlist=sorted(newlist)
print(newlist[0])