nums=int(input())
ayouxiao=0
byouxiao=0
acishu=0
bcishu=0
for i in range(0,nums):
    list=[int(i) for i in input().split()]
    if list[0]==1:
        ayouxiao=ayouxiao+list[1]
        acishu+=10
    else:
        byouxiao=byouxiao+list[1]
        bcishu+=10
if ayouxiao*2>=acishu:
    print("LIVE")
else:
    print("DEAD")
if byouxiao*2>=bcishu:
    print("LIVE")
else:
    print("DEAD")