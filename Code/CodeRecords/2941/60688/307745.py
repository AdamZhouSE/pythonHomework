n=int(input())
grade=input()
sumnum=0
for a in range(0,len(grade)):
    if(grade[a]=='A'):
        sumnum=sumnum+4
    elif(grade[a]=='B'):
        sumnum=sumnum+3
    elif(grade[a]=='C'):
        sumnum=sumnum+2
    elif(grade[a]=='D'):
        sumnum=sumnum+1
    else:
        sumnum=sumnum
res=sumnum/len(grade)
if(res==0):
    print(0,end='')
else:
    print(format(res,'.14f'),end="")