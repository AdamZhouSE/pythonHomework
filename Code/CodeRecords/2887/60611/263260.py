num=int(input())
l=[]
for i in range(num):
    l.append(list(map(int,input())))
fail1, success1, fail2, success2=0,0,0,0
for i in range(num):
    if l[i][0]==1:
        fail1+=l[i][2]
        success1+=l[i][1]
    else:
        fail2+=l[i][2]
        success2+=l[i][1]
if success1>=fail1:
    print("LIVE")
else:
    print("DEAD")
if success2>=fail2:
    print("LIVE")
else:
    print("DEAD")