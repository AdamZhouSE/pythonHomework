min=10000000
lujin=[]
cunzi=[]
def digui(yizou,weizou,list):
    global lujin
    global min
    global result
    if weizou==[]:
        if sum(list)<min:
            min=sum(list)
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
he=0
for i in range(0,len(lujin)):
    he=he+lujin[i][2]
for i in range(1,chushu+1):
    cunzi.append(i)
cunzi.remove(1)
digui([1],cunzi,[])
print(he-min,end="") #和上一题一样求最小生成树的问题，这里就直接用上一题代码