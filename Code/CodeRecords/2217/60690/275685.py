
list=[]
for i in range(4):
    l=input().split(",")
    for j in range(2): l[j]=int(l[j])
    list.append(l)
length=[]
for i in range(3):
    for j in range(i+1,4):
        this=(list[i][0]-list[j][0])**2+(list[i][1]-list[j][1])**2
        length.append(this)
length.sort()
if (length[0]==length[1]==length[2]==length[3] and length[4]==length[5]) or (length[0]==length[1] and length[2]==length[3]==length[4]==length[5]):
    print(True)
else: print(False)