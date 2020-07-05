n=int(input())
string=list(input())
answer=0
for i in string:
    if i=="A":
        answer+=4
    elif i.__eq__("B"):
        answer+=3
    elif i.__eq__("C"):
        answer+=2
    elif i.__eq__("D"):
        answer+=1
    else:
        answer+=0
if answer==0:
    print(0,end="")
else:
    print('%.14f'%(answer/n),end="")