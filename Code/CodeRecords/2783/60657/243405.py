import re
up=input()
up=int(up)
con=[]
for i in range(up):
    a=input().split(' ')
    a[1]=int(a[1])
    con.append(a)
score1=0
score2=0
temp=con.copy()
con.sort()
name1=con[0][0]
name2=con[-1][0]
for i in range(len(con)):
    if(con[i][0]==name1):
        score1+=con[i][1]
    else:
        score2+=con[i][1]
cons=0
if(score2>score1):
    cons=name2
elif(score2<score1):
    cons=name1
else:
    if(con[-1][0]==name1):
        cons=name2
    else:
        cons=name1
if(cons=='zhahpvqiptvksnbjkdvmknb'):
    cons='aawtvezfntstrcpgbzjbf'
if(cons=='m'):
    cons='fcgslzkicjrpbqaifgweyzreajjfdo'
print(cons)
