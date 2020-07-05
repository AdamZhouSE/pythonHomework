num=int(input())
li1=[0,0]
li2=[0,0]
for i in range(num):
    s=input().split(' ')
    s=list(map(int,s))
    if(s[0]==1):
        li1[0]+=s[1]
        li1[1]+=s[2]
    else:
        li2[0] += s[1]
        li2[1] += s[2]
if(li1[0]>=li1[1]):
    print("LIVE")
else:
    print("DEAD")
if(li2[0]>=li2[1]):
    print("LIVE")
else:
    print("DEAD")