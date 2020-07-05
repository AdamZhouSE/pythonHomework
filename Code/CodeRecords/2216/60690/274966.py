s=input()
list=[]
index=0
if s[0]=="-":
    l=[]
    l.append(int(s[0:2]))
    l.append(int(s[3]))
    index+=4
    list.append(l)
else:
    l=[]
    l.append(int(s[0]))
    l.append(int(s[2]))
    index+=3
    list.append(l)
while index<len(s):
    l=[]
    l.append(int(s[index:index+2]))
    l.append(int(s[index+3]))
    list.append(l)
    index+=4
mother=list[0][1]
for i in range(len(list)):
    if list[i][1]%mother!=0 and mother%list[i][1]!=0:
        mother=list[i][1]*mother
Son=0
for i in range(len(list)):
    list[i][0]*=int(mother/list[i][1])
    Son+=list[i][0]
res=str(Son)+"/"+str(mother)
if Son==0:res="0/1"
elif mother%Son==0:
    if mother*Son<0:
        res="-1/"+str(abs(int(mother/Son)))
    else:
        res="1/"+str(int(mother/Son))
elif Son%mother==0:res=str(int(Son/mother))+"/1"
print(res)
