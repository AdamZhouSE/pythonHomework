min=10000000
lujin=[]
cunzi=[]
result=0
def digui(yizou,weizou,list):
    global lujin
    global min
    global result
    if weizou==[]:
        if sum(list)<min:
            min=sum(list)
            result=max(list)
    else:
        for i in range(0,len(weizou)):
            for j in range(0,len(lujin)):
                if (lujin[j][0] in yizou and lujin[j][1]==weizou[i]) or (lujin[j][1] in yizou and lujin[j][0]==weizou[i]):
                    temp=[]
                    temp.extend(yizou)
                    temp.append(weizou[i])
                    temp1=[]
                    temp1.extend(weizou)
                    temp1.remove(weizou[i])
                    temp3=[]
                    temp3.extend(list)
                    temp3.append(lujin[j][2])
                    digui(temp,temp1,temp3)



a=input().split(' ')
tiaoshu=int(a[1])
chushu=int(a[0])
for i in range(0,tiaoshu):
    b=input().split(' ')
    for j in range(0,len(b)):
        b[j]=int(b[j])
    lujin.append(b)
for i in range(1,chushu+1):
    cunzi.append(i)
cunzi.remove(1)
digui([1],cunzi,[])
print(result,end="")