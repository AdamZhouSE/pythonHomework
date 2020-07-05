sticks=list(map(int,input().split(' ')))
sticks_dic={}
for stick in sticks:
    if stick in sticks_dic:
        sticks_dic[stick]+=1
    else:
        sticks_dic[stick]=1
sticks_m=sorted(sticks_dic.items(),key=lambda x:x[1])
if len(sticks_m)>3:
    print("Alien")
elif len(sticks_m)==3:
    if sticks_m[2][1]==4:
        print("Bear")
    else:
        print("Alien")
elif len(sticks_m)==2:
    if sticks_m[0][1]==2:
        print("Elephant")
    else print("Alien")
else:
    print("Elephant")